from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    prize = models.CharField(max_length=200)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rules = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateField()
    
    def __str__(self):
        return self.title

class user_challenge(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Entries(models.Model):
    total = models.IntegerField()
    streak = models.IntegerField(default = '0')
    today = models.DateField()
    challenge = models.ForeignKey(Challenge,on_delete=models.CASCADE)
    competitor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
