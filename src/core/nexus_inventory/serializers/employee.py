from rest_framework.serializers import ModelSerializer

from core.nexus_inventory.models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1