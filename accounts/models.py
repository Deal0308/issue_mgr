from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model
from issues.models import Status, Issue




# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return self.username
    

    

