from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from forumApp import views 

router=DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns=[
    path('', include(router.urls))
]