from django.contrib import admin

from core.nexus_inventory.models import AssetHistory

@admin.register(AssetHistory)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_type', 'action_date', 'employee')
    search_fields = ('action_type', 'employee',)
    ordering = ('-action_date',)