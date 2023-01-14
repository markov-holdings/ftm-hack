from rest_framework import generics, permissions, authentication, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, ChangePasswordSerializer

## CRUD for User model

class UserChangePasswordAPIView(generics.UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        name = serializer.validated_data.get("name") or None

        if name is None:
            name = email
        serializer.save()

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        # update some fields

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    lookup_field = "pk"
    
    def perform_destroy(self, instance):
        # instance do someting
        return super().perform_destroy(instance)