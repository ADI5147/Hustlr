from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    USER_ROLES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    bio = models.CharField(max_length=200, blank=True)
    portfolio_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
