from rest_framework.viewsets import ModelViewSet

from core.nexus_inventory.models import Asset
from core.nexus_inventory.serializers import AssetSerializer, AssetDetailSerializer, AssetListSerializer

class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return AssetListSerializer
        elif self.action == "retrieve":
            return AssetDetailSerializer
        return AssetSerializer