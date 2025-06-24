from rest_framework import viewsets
from .models import Job, Bid
from .serializers import JobSerializer, BidSerializer
from rest_framework.permissions import IsAuthenticated

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]