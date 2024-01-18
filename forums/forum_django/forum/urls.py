from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from . import views
from django.contrib import admin
from .views import RegisterView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/register/', RegisterView.as_view(), name='register_view'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]