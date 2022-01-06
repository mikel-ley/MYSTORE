from django.contrib import admin
from django.db import router
from django.urls import path, include
from peliculas import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from films import views as film_views


router = routers.DefaultRouter()
# En el router vamos añadiendo los endpoints a los viewsets
router.register('peliculas', views.PeliculaViewSet)
router.register('films', film_views.FilmViewSet, basename='Film')
router.register('genres',film_views.GenreViewSet, basename='FilmGenre')
router.register('FilmUsuario', film_views.FilmUsuarioViewSets, basename='FilmUsuario') 
router.register('Config', film_views.ConfigViewSets, basename='Config') 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('api/', include(router.urls)),

    #Ruta de 
    path('peliculas/v1/favorita/', views.MarcarPeliculaFavorita.as_view()),
    path('peliculas/v1/favoritas/', views.ListarPeliculasFavoritas.as_view()),

]

if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

