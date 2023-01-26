import uuid
import boto3 
from botocore.config import Config


class HeadlessLexClient:
    def __init__(self, botId, botAliasId):
        self.config = {
            "aws_region": "us-west-2",
        }
 
        self.boto_config = Config(
            region_name = self.config['aws_region']
        )

        self.client = boto3.client('lexv2-runtime', config=self.boto_config)

        self.botId = botId
        self.botAliasId = botAliasId
        self.localeId = "en_US"
        self.sessionId = uuid.uuid4().hex

        print("------------ Chat ------------")


    def post(self, msg):
        response = self.client.recognize_text(
            botId=self.botId,
            botAliasId=self.botAliasId,
            localeId=self.localeId,
            sessionId=self.sessionId,
            text=msg,                    
        )

        replies = ["Bot: " + msg["content"] for msg in response["messages"]]
        return replies

if __name__ == "__main__":
    client = HeadlessLexClient("FQGWQ4WMEM", "TSTALIASID")

    while True:
        msg = input("You: ")
        replies = client.post(msg)
        print("\n".join(replies))