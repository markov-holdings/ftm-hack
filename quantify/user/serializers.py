from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field="pk",
    ) 

    class Meta:
        model = User
        fields = [ 
            'url',
            'email',
            'password',
            'name',
            'is_active',
            'is_staff',
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return super().create(validated_data)

class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)