from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('musics/', views.MusicList.as_view(), name='music-list'),
    path('music/<int:id>/', views.MusicDetail.as_view(), name='music-detail'),

    path('albuns/', views.AlbumList.as_view()),
    path('albun/<int:id>/', views.AlbumDetail.as_view()),

    path('bands/', views.BandList.as_view()),
    path('band/<int:id>/', views.BandDetail.as_view()),

     path('members/', views.MemberList.as_view()),
    path('member/<int:id>/', views.MemberDetail.as_view()),


    
]