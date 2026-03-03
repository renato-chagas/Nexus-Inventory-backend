from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.nexus_inventory.models import AssetHistory, Asset


class AssetHistorySerializer(ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    asset_name = serializers.SerializerMethodField()

    class Meta:
        model = AssetHistory
        fields = [
            "id",
            "asset",
            "asset_name",
            "action_date",
            "action_type",
            "observaitions",
            "employee",
            "employee_name",
        ]

    def get_employee_name(self, obj):
        if obj.employee:
            return f"{obj.employee.name} {obj.employee.surname}"
        return None

    def get_asset_name(self, obj):
        if obj.asset:
            return obj.asset.name

        if obj.employee:
            asset = Asset.objects.filter(person_in_charge=obj.employee).first()
            if asset:
                return asset.name

        return None
