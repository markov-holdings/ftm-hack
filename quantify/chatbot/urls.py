from django.urls import path
from . import views

urlpatterns = [
    path("", views.ChatbotListCreateAPIView.as_view(), name="chatbot-list"),
    path("<int:pk>/update/", views.ChatbotUpdateAPIView.as_view(), name="chatbot-update"),
    path("<int:pk>/delete/", views.ChatbotDeleteAPIView.as_view(), name="chatbot-delete"),
    path("<int:pk>/", views.ChatbotDetailAPIView.as_view(), name="chatbot-detail"),
    path("<int:pk>/build/", views.ChatbotBuildAPIView.as_view(), name="chatbot-build"),                                                     
]