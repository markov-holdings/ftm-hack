from dataclasses import dataclass
import requests
from getpass import getpass
import pathlib 
import json


@dataclass
class JWTClient:
    """
    Use a dataclass decorator
    to simply the class construction
    """
    access:str = None
    refresh:str = None
    # ensure this matches your simplejwt config
    header_type: str = "Bearer"
    # this assumesy ou have DRF running on localhost:8000
    base_endpoint = "http://localhost:8000/api"
    # this file path is insecure
    cred_path: pathlib.Path = pathlib.Path("creds.json")

    def __post_init__(self):
        if self.cred_path.exists(): 
            """
            You have stored creds,
            let's verify them
            and refresh them.
            If that fails,
            restart login process.
            """
            try:
                data = json.loads(self.cred_path.read_text())
            except Exception:
                print("Assuming creds has been tampered with")
                data = None
            if data is None:
                """ 
                Clear stored creds and
                Run login process
                """
                self.clear_tokens()
                self.perform_auth()
            else:
                """
                `creds.json` was not tampered with
                Verify token -> 
                if necessary, Refresh token ->
                if necessary, Run login process
                """
                self.access = data.get('access')
                self.refresh = data.get('refresh')
                token_verified = self.verify_token()
                if not token_verified:
                    """
                    This can mean the token has expired
                    or is invalid. Either way, attempt
                    a refresh.
                    """
                    refreshed = self.perform_refresh()
                    if not refreshed:
                        """
                        This means the token refresh
                        also failed. Run login process
                        """
                        print("invalid data, login again.")
                        self.clear_tokens()
                        self.perform_auth()
        else:
            """
            Run login process
            """
            self.perform_auth()

    def get_headers(self, header_type=None):
        """
        Default headers for HTTP requests
        including the JWT token
        """
        _type = header_type or self.header_type
        token = self.access
        if not token:
            return {}
        return {
                "Authorization": f"{_type} {token}"
        }

    def perform_auth(self):
        """
        Simple way to perform authentication
        Without exposing password(s) during the
        collection process.
        """
        endpoint = f"{self.base_endpoint}/token/" 
        username = input("What is your username?\n")
        password = getpass("What is your password?\n")
        r = requests.post(endpoint, json={'email': username, 'password': password}) 
        if r.status_code != 200:
            raise Exception(f"Access not granted: {r.text}")
        print('access granted')
        self.write_creds(r.json())

    def write_creds(self, data:dict):
        """
        Store credentials as a local file
        and update instance with correct
        data.
        """
        if self.cred_path is not None:
            self.access = data.get('access')
            self.refresh = data.get('refresh')
            if self.access and self.refresh:
                self.cred_path.write_text(json.dumps(data))

    def verify_token(self):
        """
        Simple method for verifying your
        token data. This method only verifies
        your `access` token. A 200 HTTP status
        means success, anything else means failure.
        """
        data = {
            "token": f"{self.access}"
        }
        endpoint = f"{self.base_endpoint}/token/verify/" 
        r = requests.post(endpoint, json=data)
        return r.status_code == 200

    def clear_tokens(self):
        """
        Remove any/all JWT token data
        from instance as well as stored
        creds file.
        """
        self.access = None
        self.refresh = None
        if self.cred_path.exists():
            self.cred_path.unlink()

    def perform_refresh(self):
        """
        Refresh the access token by using the correct
        auth headers and the refresh token.
        """
        print("Refreshing token.")
        headers = self.get_headers()
        data = {
            "refresh": f"{self.refresh}"
        }
        endpoint = f"{self.base_endpoint}/token/refresh/" 
        r = requests.post(endpoint, json=data, headers=headers)
        if r.status_code != 200:
            self.clear_tokens()
            return False
        refresh_data = r.json()
        if not 'access' in refresh_data:
            self.clear_tokens()
            return False
        stored_data = {
            'access': refresh_data.get('access'),
            'refresh': self.refresh
        }
        self.write_creds(stored_data)
        return True

    def list(self, endpoint=None, limit=3):
        headers = self.get_headers()
        if endpoint is None or self.base_endpoint not in str(endpoint):
            endpoint = f"{self.base_endpoint}/chatbot/?limit={limit}" 
        r = requests.get(endpoint, headers=headers) 
        if r.status_code != 200:
            raise Exception(f"Request not complete {r.text}")
        data = r.json()
        return data
    
    def detail(self, endpoint, id=1):
        headers = self.get_headers()
        if endpoint is None or self.base_endpoint not in str(endpoint):
            endpoint = f"{self.base_endpoint}/chatbot/{id}"
        r = requests.get(endpoint, headers=headers) 
        if r.status_code != 200:
            raise Exception(f"Request not complete {r.text}")
        return r.json()

    def create(self, endpoint, data):
        headers = self.get_headers()
        r = requests.post(endpoint, headers=headers, json=data)
        return r.json()
    
    def update(self, endpoint, data):
        headers = self.get_headers()
        r = requests.put(endpoint, headers=headers, json=data)
        return r.json()
    
    def delete(self, endpoint):
        headers = self.get_headers()
        r = requests.delete(endpoint, headers=headers)
        if r.status_code == 204:
            return "Success"
        else:
            return r.status_code

if __name__ == "__main__":
    client = JWTClient() 
    data = None

    # show all bots
    data = client.list("http://localhost:8000/api/chatbot", limit=5) 
    
    # show single bot
    #data = client.detail("http://localhost:8000/api/chatbot/7/") 
    
    # create new bot
    #'''
    data = client.create("http://localhost:8000/api/chatbot/", 
                         data={
                             "name": "FloristBot",
                             "social_media_type": "instagram",
                             "content":"absdbajaksbdsa",
                            }
                         ) 
    #'''
    # update bot 
    #data = client.update("http://localhost:8000/api/chatbot/7/update/", data={"name": "New bot name", "social_media_type":"instagram", "content":"asdfgh"})
    
    # delete bot
    #data = client.delete("http://localhost:8000/api/chatbot/1/delete/")
    
    print(data)