from rest_framework import serializers
from .models import Chatbot
from user.serializers import UserPublicSerializer

class ChatbotSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='chatbot-detail',
        lookup_field="pk",
    ) 

    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Chatbot
        fields = [ 
            'url',
            'owner',
            'name',
            'social_media_type',
            'content',
        ]

    def create(self, validated_data):
        return super().create(validated_data)