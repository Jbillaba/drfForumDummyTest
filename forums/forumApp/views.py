from rest_framework import viewsets
from forumApp.models import Post
from forumApp.serializers import PostSerializer
from forumApp.serializers import UserSerializer
from django.contrib.auth.models import User 

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
    enables full crud support 
    """
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(op=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer