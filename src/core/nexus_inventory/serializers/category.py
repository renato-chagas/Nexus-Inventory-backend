from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from core.nexus_inventory.models import Category

class CategorySerializer(ModelSerializer):
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_quantity(self, obj):
        return obj.quantity
    