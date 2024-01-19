from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timesince

class User(AbstractUser):
    username=models.CharField(max_length=30, unique=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=60, unique=True)
    password=models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Post(models.Model):
    title=models.CharField(max_length=100, default='')
    text=models.TextField(max_length=255)
    op=models.ForeignKey(User, on_delete=models.CASCADE, related_name='originalposter')
    created_on=models.DateTimeField(auto_now_add=True)

    @property
    def timesince(self):
        return timesince.timesince(self.created_on)

    def __str__(self):
        return self.title
    