from django.contrib import admin
from galeria.models import Image

class ShowImage(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption', 'published')
    list_display_links = ('id', 'name', 'caption')
    search_fields = ('name',)
    list_editable = ('published',)
    list_filter = ('category',)

# Register your models here.
admin.site.register(Image, ShowImage)