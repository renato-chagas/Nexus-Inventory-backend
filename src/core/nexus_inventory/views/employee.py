from rest_framework.viewsets import ModelViewSet

from core.nexus_inventory.models import Employee
from core.nexus_inventory.serializers import EmployeeSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer