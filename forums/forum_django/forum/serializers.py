from .models import User, Post, Comment
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.humanize.templatetags.humanize import naturaltime


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2=serializers.CharField(write_only=True, required=True)

    class Meta:
        model=User
        fields=['username', 'name', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError(
                {'password':"Password fields didn't match"})

        return attrs

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
    op=serializers.SerializerMethodField("get_op")
    created_on=serializers.SerializerMethodField("get_timesince")
    class Meta:
        model=Post
        fields=['url', 'id', 'title', 'text', 'op', 'created_on']
    
    def get_op(self, object):
        return object.op.username
    
    def get_timesince(self, object):
        return naturaltime(object.created_on)
    
    def create(self, validated_data):
        validated_data['op']=self.context['request'].user
        return super(PostSerializer, self).create(validated_data)
    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    op=serializers.SerializerMethodField("get_op")
    created_on=serializers.SerializerMethodField("get_timesince")
    class Meta:
        model=Comment
        fields=['op', 'text', 'post', 'created_on']
    def get_op(self, object):
        return object.op.username
    def get_timesince(self, object):
        return naturaltime(object.created)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, User):
        token=super().get_token(User)

        #add custom claims
        token['username']=User.username
        token['email']=User.email
        token['name']=User.name

        return token