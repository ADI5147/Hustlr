from rest_framework import serializers
from .models import Job, Bid
from accounts.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(read_only=True)
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'budget', 'category', 'posted_by', 'created_at', 'deadline']

class BidSerializer(serializers.ModelSerializer):
    freelancer = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    class Meta:
        model = Bid
        fields = ['id', 'job', 'freelancer', 'amount', 'proposal', 'created_at']