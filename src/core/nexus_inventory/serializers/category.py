from rest_framework.serializers import ModelSerializer

from core.nexus_inventory.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'