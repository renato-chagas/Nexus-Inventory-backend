from django.contrib import admin

from core.nexus_inventory.models import Software

@admin.register(Software)   
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version',)
    search_fields = ('name', 'version',)