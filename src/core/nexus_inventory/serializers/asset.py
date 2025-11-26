from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField
)

from core.nexus_inventory.models import Asset

from core.uploader.models import Image
from core.uploader.serializers.image import ImageSerializer


class AssetSerializer(ModelSerializer):
    Image_attachment_key = SlugRelatedField(
        source='image',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True
    )
    Image = ImageSerializer(required=False, read_only=True)
    
    class Meta:
        model = Asset
        fields = '__all__'
        
        
class AssetDetailSerializer(ModelSerializer):
    Image = ImageSerializer(required=False)
    
    class Meta:
        model = Asset
        fields = '__all__'
        depth = 1
    
        
class AssetListSerializer(ModelSerializer):
    Image = ImageSerializer(required=False)
    
    class Meta:
        model = Asset
        fields = ['id', 'name', 'serial_number', 'status', 'Image']