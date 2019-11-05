from django.contrib import admin
from .models import Music, Band, Member, Album

# Register your models here.
admin.site.register(Music)
admin.site.register(Band)
admin.site.register(Member)
admin.site.register(Album)
