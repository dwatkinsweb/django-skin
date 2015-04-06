from django.contrib import admin
from .models import SiteSkin


class SiteSkinAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'path')
    list_filter = ('site',)
    search_fields = ('name',)


admin.site.register(SiteSkin, SiteSkinAdmin)