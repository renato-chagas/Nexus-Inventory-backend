from rest_framework.viewsets import ModelViewSet

from core.nexus_inventory.models import Software
from core.nexus_inventory.serializers import SoftwareSerializer

class SoftwareViewSet(ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer