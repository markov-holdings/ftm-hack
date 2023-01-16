from rest_framework import generics, permissions, authentication
from .models import Chatbot, Intent, Utterance, Slot
from .serializers import ChatbotSerializer, IntentSerializer, UtteranceSerializer, SlotSerializer

## CRUD for Chatbot model

class ChatbotListCreateAPIView(generics.ListCreateAPIView):
    #queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer

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

    def get_queryset(self):
        queryset = Chatbot.objects.all()
        return queryset
            
class ChatbotUpdateAPIView(generics.UpdateAPIView):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer    
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()
        # update some fields

class ChatbotDeleteAPIView(generics.DestroyAPIView):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer    
    lookup_field = "pk"
    
    def perform_destroy(self, instance):
        # instance do someting
        return super().perform_destroy(instance)