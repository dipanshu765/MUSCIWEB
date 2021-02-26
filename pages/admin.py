from django.contrib import admin
from .models import Song

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'singer')
    list_display_links = ('title','singer')
    search_fields = ('title', 'singer', 'description')
    list_per_page = 10

admin.site.register(Song, SongAdmin)
