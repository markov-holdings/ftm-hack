from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from .models import Chatbot
from .serializers import ChatbotSerializer
from .services import LexFactoryService
from .permissions import IsOwner

## CRUD for Chatbot model

class ChatbotListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ChatbotSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            # return all chatbots
            return Chatbot.objects.all()
        else:
            # return only owned chatbots
            return Chatbot.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChatbotDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ChatbotSerializer    
    permission_classes = [IsOwner]

    def get_queryset(self):
        queryset = Chatbot.objects.all()
        return queryset
            
class ChatbotUpdateAPIView(generics.UpdateAPIView):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer    
    permission_classes = [IsOwner]
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()
        # update some fields

class ChatbotDeleteAPIView(generics.DestroyAPIView):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer    
    permission_classes = [IsOwner]
    lookup_field = "pk"
    
    def perform_destroy(self, instance):
        # instance do someting
        return super().perform_destroy(instance)

class ChatbotBuildAPIView(generics.GenericAPIView):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer    
    permission_classes = [IsOwner]
    lookup_field = "pk"

    def get_object(self, pk):
        return Chatbot.objects.get(pk=pk)

    def patch(self, request, pk):
        bot = self.get_object(pk)

        if 'bot_status' not in request.data: # check valid patch
            return Response(status=400, data="invalid parameters for PATCH, only { 'bot_status': bool } allowed")
    
        if request.data["bot_status"] == True:
            # build bot
            input = self.model_to_lex_factory_input(bot)
            lex_service = LexFactoryService(input)
            lex_service.run()
            aws_bot_id = lex_service.get_aws_bot_id()

            request.data["aws_bot_id"] = aws_bot_id
            serializer = ChatbotSerializer(bot, data=request.data, partial=True, context={'request': request})

        elif request.data["bot_status"] == False:
            # kill bot
            serializer = ChatbotSerializer(bot, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=serializer.data)
        
        return Response(status=400, data="invalid parameters for chatbot PATCH")
  
    def model_to_lex_factory_input(self, bot) -> dict:
        # unpack model data to input for LexFactoryService constructor
        input = {}
        input["name"] = bot.name
        input["description"] = bot.description
        input["chatbot_intents"] = []
        for intent in bot.chatbot_intents.all():
            intent_data = {}
            intent_data["name"] = intent.name
            intent_data["description"] = intent.description

            intent_data["utterances"] = []
            for utterance in intent.utterances.all():
                intent_data["utterances"].append({"utterance" : utterance.content})

            intent_data["slots"] = []    
            for slot in intent.slots.all():
                intent_data["slots"].append({"name": slot.name, "content" : slot.content, "options": slot.options})

            input["chatbot_intents"].append(intent_data)

        return input
