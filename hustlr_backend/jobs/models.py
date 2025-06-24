from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
    
#for bid
class Bid(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='bids')
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    proposal = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid by {self.freelancer.username} on {self.job.title}"