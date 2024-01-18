from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from . import views
from django.contrib import admin
from .views import RegisterView

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/register/', RegisterView.as_view(), name='register_view')
]