from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.nexus_inventory.models import AssetHistory
from core.nexus_inventory.serializers import AssetHistorySerializer


class AssetHistoryViewSet(ModelViewSet):
    queryset = AssetHistory.objects.all()
    serializer_class = AssetHistorySerializer
    permission_classes = [IsAuthenticated]
