from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from core.nexus_inventory.models import Asset
from core.nexus_inventory.serializers import AssetSerializer, AssetDetailSerializer, AssetListSerializer

class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "serial_number", "status", "category", "person_in_charge"]
    search_fields = ["name", "serial_number", "status"]
    ordering_fields = ["name", "created_at", "updated_at"]
    ordering = ["name"]
    
    def get_serializer_class(self):
        if self.action == "list":
            return AssetListSerializer
        elif self.action == "retrieve":
            return AssetDetailSerializer
        return AssetSerializer