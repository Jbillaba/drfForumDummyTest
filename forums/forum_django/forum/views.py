from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import User, Post
from .serializers import UserSerializer, PostSerializer, RegisterSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=(AllowAny)