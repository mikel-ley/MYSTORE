from django.db import models
from django.contrib.auth.models import AbstractUser

def path_to_avatar(instance, filename):
    return f'avatars/{instance.id}/{filename}'


    
#
