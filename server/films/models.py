from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Film(models.Model):
    def path_to_film(instance, filename):
        return f'films/{instance.id}/{filename}'


    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=150,verbose_name="Titulo")
    year  = models.PositiveBigIntegerField(default=2000, verbose_name="Año")
    review_short = models.TextField(null=True,blank=True, verbose_name="Argumento(corto)")
    review_large = models.TextField(null=True, blank=True, verbose_name="Historia(largo)")
    trailer_url = models.URLField(max_length=150, null=True, blank=True, verbose_name="URL en Youtube")
    genres = models.ManyToManyField('FilmGenre', related_name="film_genres", verbose_name="Generos")
    image_thumbnail = models.ImageField(upload_to = 'films/', null = True, blank = True, verbose_name="Miniatura")
    image_wallpaper = models.ImageField(upload_to = 'films/', null = True, blank = True, verbose_name="Wallpaper")
   
    class Meta:
        verbose_name="Pelicula" 
        ordering = ['title']

    def __str__(self):
        return f'{self.title} ({self.year})'

class FilmGenre(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name="Genero"
        ordering = ['name']

    def __str__(self):
        return f'{self.name})'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FilmGenre, self).save(*args, **kwargs)
    
class FilmUsuario(models.Model):
    film = models.ForeignKey (Film,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    vista = models.PositiveIntegerField(default=0)
    estado = models.PositiveIntegerField(default=1)


class Config(models.Model):
    nombre_del_cien = models.CharField(max_length=150,verbose_name="Titulo")
    direcion= models.CharField(max_length=150,verbose_name="Titulo")
    estado = models.PositiveIntegerField(default=1) 
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
        
    
# crear otro modulo y clasificar peliculas, crear un nuevo modulo y mandar a llamar la base de datos 