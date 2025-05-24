from django.contrib import admin
from .models import Advertisement, AdImage

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'owner')
    search_fields = ('title', 'description')

admin.site.register(Advertisement, AdvertisementAdmin)

class AdImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'advertisement')
    search_fields = ('image', 'advertisement')

admin.site.register(AdImage, AdImageAdmin)
