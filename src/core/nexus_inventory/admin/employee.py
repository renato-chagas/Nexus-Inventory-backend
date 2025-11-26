from django.contrib import admin

from core.nexus_inventory.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'phone', 'department', 'hire_date')
    search_fields = ('name', 'surname', 'email', 'department')
    ordering = ('surname', 'name')
