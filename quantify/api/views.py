from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"invalid": "invalid data"}, status=400)