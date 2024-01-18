from .models import User, Post
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

## TODO: finish this file 

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model=User
        fields=['username', 'name', 'email', 'password']
    
    def create(self, validated_data):
        user=User.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url', 'id', 'username', 'name', 'email', 'password']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Post
        fields=['url', 'id', 'title', 'text', 'op']