from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

#Importar Selializer
from .serializers import UserSerializer

from django.contrib.auth import get_user_model

class LoginView(APIView):
    def post(self, request):
        #Obtener email y password
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        #Autenticar Usuario
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            
        return Response(
            status = status.HTTP_404_NOT_FOUND
        )


class LogoutView(APIView):
    def post(self, request):
        #Metodo que borra la info del usuario
        logout(request)

        #Respuesta al usuario
        return Response(
                status= status.HTTP_200_OK
            )


#Crear Usuario
class SingupView(generics.CreateAPIView):
    serializer_class = UserSerializer

@receiver(reset_password_token_created)
def password_reset_token_create(sender, instance, reset_password_token, *args,**kwargs):
    print(f"\nRecupera la contraseña de el correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API: http://localhost:8000/api/auth/reset/confirm/.\n\n")
    
    #Proximamente
    #f"Tambien puedes hacerlo directamente desde la aplicacion web en http://localhost:3000/new-password/token={reset_password_token.key}"
    