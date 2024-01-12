from rest_framework import serializers 
from forumApp.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.HyperlinkedModelSerializer):
    op=serializers.ReadOnlyField(source='op.username')

    class Meta:
        model=Post
        fields=['url', 'id', 'op', 'title', 'textarea']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts=serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model=User
        fields=['url', 'id', 'username', 'posts']