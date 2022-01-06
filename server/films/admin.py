from django.contrib import admin
from .models import Film, FilmGenre, Question


#Register your models here.

admin.site.register(Film)
class FildAdmin(admin.ModelAdmin):
   pass

admin.site.register(FilmGenre)
class FilmGenreAdmin(admin.ModelAdmin):
   readonly_fields = ["slug"]
   

admin.site.register(Question)

