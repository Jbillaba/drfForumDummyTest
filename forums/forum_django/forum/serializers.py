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
    account_created=serializers.SerializerMethodField("get_time_since_creation")
    class Meta:
        model=User
        fields=['url', 'id', 'username', 'name', 'email', 'account_created' ,'password']
    
    def get_time_since_creation(self, object):
        return naturaltime(object.created_on)


    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    op=serializers.SerializerMethodField("get_op")
    posted_on=serializers.SerializerMethodField("get_post_id")
    created_on=serializers.SerializerMethodField("get_timesince")
    class Meta:
        model=Comment
        fields=['url','id','op', 'text', 'post', 'posted_on' , 'created_on', ]
    
    def get_op(self, object):
        return object.op.username
    
    def get_timesince(self, object):
        return naturaltime(object.created_on)
    
    def get_post_id(self, object):
        return object.post.id
    
    def create(self, validated_data):
        validated_data['op']=self.context['request'].user
        return super(CommentSerializer, self).create(validated_data)

class PostSerializer(serializers.HyperlinkedModelSerializer):
    op=serializers.SerializerMethodField("get_op")
    created_on=serializers.SerializerMethodField("get_timesince")
    number_of_comments=serializers.SerializerMethodField("get_number_of_comments")
    class Meta:
        model=Post
        fields=['url', 'id', 'title', 'text', 'op', 'created_on', 'number_of_comments' ]
    
    def get_op(self, object):
        return object.op.username
    
    def get_timesince(self, object):
        return naturaltime(object.created_on)
    
    def get_number_of_comments(self, object):
        comments=Comment.objects.all()
        return comments.filter(post=object.id).count()
    
    def create(self, validated_data):
        validated_data['op']=self.context['request'].user
        return super(PostSerializer, self).create(validated_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, User):
        token=super().get_token(User)

        #add custom claims
        token['username']=User.username
        token['email']=User.email
        token['name']=User.name

        return token