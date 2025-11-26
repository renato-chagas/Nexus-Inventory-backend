from django.contrib import admin

from core.nexus_inventory.models import Asset

@admin.register(Asset)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number', 'status', 'bought_price', 'bought_date', 'category', 'person_in_charge')
    search_fields = ('name', 'serial_number', 'status', 'category', 'person_in_charge')
    list_per_page = 10