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
    social_media_type = models.CharField(max_length=20, choices=SOCIAL_MEDIA_TYPE_CHOICES)
    
    # AWS Lex fields
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    aws_bot_id = models.CharField(max_length=50, default=-1)
    bot_status = models.BooleanField(default=False) # is bot available
    locale_status = models.BooleanField(default=False) # is bot built

class Intent(models.Model):
    chatbot = models.ForeignKey(Chatbot, null=True, on_delete=models.CASCADE, editable=True, related_name='chatbot_intents')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Utterance(models.Model):
    intent = models.ForeignKey(Intent, null=True, on_delete=models.CASCADE, editable=True, related_name="utterances")
    content = models.TextField(blank=False)

class Slot(models.Model):
    intent = models.ForeignKey(Intent, null=True, on_delete=models.CASCADE, editable=True, related_name="slots")
    content = models.TextField(blank=False)