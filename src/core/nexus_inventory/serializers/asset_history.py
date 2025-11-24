from rest_framework.serializers import ModelSerializer

from core.nexus_inventory.models import AssetHistory

class AssetHistorySerializer(ModelSerializer):
    class Meta:
        model = AssetHistory
        fields = '__all__'