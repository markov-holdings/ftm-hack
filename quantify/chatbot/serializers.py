from rest_framework import serializers
from .models import Chatbot, Intent, Utterance, Slot
from user.serializers import UserPublicSerializer

class UtteranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utterance
        fields = '__all__'
    
class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

class IntentSerializer(serializers.ModelSerializer):
    utterances = UtteranceSerializer(many=True)
    slots = SlotSerializer(many=True)
    
    class Meta:
        model = Intent
        fields = [
            'chatbot',
            'utterances',
            'slots',
            'name',
            'description',
        ]
    
    def create(self, validated_data):
        utterances = validated_data.pop('utterances')
        slots = validated_data.pop('slots')

        intent_instance = Intent.objects.create(**validated_data)

        for utterance in utterances:
            Utterance.objects.create(intent=intent_instance, **utterance)
        for slot in slots:
            Slot.objects.create(intent=intent_instance, **slot)

        return intent_instance

class ChatbotSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='chatbot-detail',
        lookup_field="pk",
    ) 

    chatbot_intents = IntentSerializer(many=True)
    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Chatbot
        fields = [ 
            'url',
            'owner',
            'chatbot_intents',
            'name',
            'description',
            'social_media_type',
            'aws_bot_id',
            'bot_status',
            'locale_status',
        ]

    def create(self, validated_data):
        chatbot_intents = validated_data.pop('chatbot_intents')
        chatbot_instance = Chatbot.objects.create(**validated_data)
        for intent in chatbot_intents:
            utterances = intent.pop('utterances')
            slots = intent.pop('slots')

            intent_instance = Intent.objects.create(chatbot=chatbot_instance, **intent)

            for utterance in utterances:
                Utterance.objects.create(intent=intent_instance, **utterance)
            for slot in slots:
                Slot.objects.create(intent=intent_instance, **slot)

        return chatbot_instance