from django.core.paginator import Page
from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework import pagination
from .models import Film, FilmGenre
from .serializers import FilmSerializer, FilmGenreSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ExtencedPagination(PageNumberPagination):
    page_size = {}
    def get_paginated_response(self, data):
        return Response({'count':self.page.paginator.count,
        'num_pages':self.page.paginator.num_pages,
        'page_number':self.page.number,
        'page_size':self.page_size,
        'next_link':self.get_next_link(),
        'previous_link':self.get_previous_link(),
        'results':data})



class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= Film.objects.all()
    serializer_class = FilmSerializer
    #Filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'year', 'genres__name']
    ordering_fields = ['title','year']
    filters_fields = {'year':['lte', 'gte'], 'genres':['exact']}
    #Sistema de paginacion
    
    pagination_class = ExtencedPagination
    #pagination_class = PageNumberPagination
    #pagination_class.page_size = 8



class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= FilmGenre.objects.all()
    serializer_class = FilmGenreSerializer
    lookup_field = 'slug'


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= FilmGenre.objects.all()
    serializer_class = FilmGenreSerializer
    lookup_field = 'slug'
    
class FilmUsuarioViewSets(viewsets.ModelViewSet):
    queryset= FilmGenre.objects.all()
    serializer_class = FilmGenreSerializer
    lookup_field = 'slug'

class ConfigViewSets(viewsets.ModelViewSet):
    queryset= FilmGenre.objects.all()
    serializer_class = FilmGenreSerializer
    lookup_field = 'slug'

  
    
