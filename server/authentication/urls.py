from django.urls import path
from django.urls.conf import include
from .views import LogoutView, LoginView, SingupView

urlpatterns = [
    path('auth/login',LoginView.as_view(), name='auth_login'),
    path('auth/logout',LogoutView.as_view(), name='auth_logout'),
    path('auth/singup',SingupView.as_view(), name = 'auth_singup'),
    path('auth/reset', include('django_rest_passwordreset.urls'), name='password_reset'),
]