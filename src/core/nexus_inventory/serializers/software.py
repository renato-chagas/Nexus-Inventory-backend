from rest_framework.serializers import ModelSerializer

from core.nexus_inventory.models import Software

class SoftwareSerializer(ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'