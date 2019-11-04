from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('musics/', views.MusicList.as_view(), name='music-list'),
    
]