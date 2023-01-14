from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Chatbot(models.Model):
    SOCIAL_MEDIA_TYPE_CHOICES = (
        ("instagram", "INSTAGRAM"),
        ("messenger", "MESSENGER"),
        ("telegram", "TELEGRAM"),
        ("whatsapp", "WHATSAPP"),
    )

    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=50)
    social_media_type = models.CharField(max_length=20, choices=SOCIAL_MEDIA_TYPE_CHOICES)
    
    # AWS Lex fields
    #dataPrivacy = models.BooleanField(default=False)
    #idleSessionTTLInSeconds = models.IntegerField(default=300)
    #roleArn = models.CharField(max_length=50, default="")
    #AWSBotId = models.CharField(max_length=50, default="") 
    #AWSBotStatus = models.BooleanField(default=False)
    
    # bot intents 
    content = models.TextField(blank=True, null=True)

    

