from rest_framework import serializers
from .models import Config, FilmGenre, FilmUsuario, Film


class FilmUsuarioserializers(serializers.ModelSerializer):
    class Meta:
        model = FilmUsuario
        fields = ['film','user','vista', 'estado']  
        
class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__' 


    

    
       # genres = FilmGenreSerializer(many=True)

# class NestedFilmGenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FilmGenre
#         fields = '__all__'

# genres = NestedFilmGenreSerializer(many=True)

# #films = NestedFilmSerializer(many=True, source="film_genres")

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class  FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmGenre
        fields = '__all__'

#     genres = FilmGenreya
