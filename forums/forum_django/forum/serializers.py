from .models import User, Post
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=[]