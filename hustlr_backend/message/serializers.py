from rest_framework import serializers
from .models import Message
from accounts.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'sent_at']