from rest_framework.viewsets import ModelViewSet

from core.nexus_inventory.models import Category
from core.nexus_inventory.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
