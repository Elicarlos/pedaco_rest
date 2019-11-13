from .models import Music, Band, Member, Album
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer): 
    album = AlbumSerializer()  
    class Meta:
        model = Music
        fields = ('title', 'seconds', 'album')


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


