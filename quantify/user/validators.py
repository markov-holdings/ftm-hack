from rest_framework import serializers
from .models import User

def validate_email(value):
    qs = User.objects.filter(email__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{qs} is already registered. Please log in or change password")
    else:
        return value
