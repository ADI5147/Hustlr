from rest_framework import serializers
from .models import Payment
from accounts.serializers import UserSerializer

class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'transaction_type', 'status', 'created_at']