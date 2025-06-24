from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)