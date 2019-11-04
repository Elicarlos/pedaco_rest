from django.shortcuts import render
from rest_framework import generics
from .models import Music
from .serializer import MusicSerializer


class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

