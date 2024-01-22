from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import User, Post
from .serializers import UserSerializer, PostSerializer, RegisterSerializer, MyTokenObtainPairSerializer
from  rest_framework_simplejwt.views import TokenObtainPairView

#Login User 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=(AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)


