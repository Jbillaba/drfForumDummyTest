from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username=models.CharField(max_length=11, unique=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Post(models.Model):
    title=models.CharField(max_length=30, default='')
    text=models.TextField()
    op=models.ForeignKey(User, on_delete=models.CASCADE, related_name='originalposter')
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    