# Developed by Vitaly Sem

"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from app import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Model views
    path('api/', include(router.urls)),

    # Rest auth
    path('', include('rest_auth.urls')),

    # Custom Signup/Login functionality
    path('sign-up/', views.signup, name="signup_user"),
    path('login/', views.login, name="login_user"),

    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('auth-jwt/', obtain_jwt_token, name="token_auth"),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
]
