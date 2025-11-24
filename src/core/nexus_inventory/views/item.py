from rest_framework.viewsets import ModelViewSet

from core.nexus_inventory.models import Item
from core.nexus_inventory.serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer