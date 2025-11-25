from django.db import models

from .category import Category
from .employee import Employee
from .software import Software
from .asset_history import AssetHistory

from core.uploader.models import Image

class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    installed_software = models.ManyToManyField('Software', blank=True)
    specs = models.TextField(blank=True, null=True)
    serial_number = models.CharField(max_length=100, unique=True)
    STATUS = [
        ('AVAILABLE','available'),
        ('IN_USE', 'in use',),
        ('MAINTENANCE', 'maintenance',),
        ('DISCARDED', 'discarded',),
    ]
    status = models.CharField(max_length=20, choices=STATUS, default='AVAILABLE ')
    bought_price = models.DecimalField(max_digits=10, decimal_places=2)
    bought_date = models.DateField()
    person_in_charge = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    asset_history = models.ManyToManyField("AssetHistory", blank=True)

    image = models.ForeignKey(
        Image,
        related_name="asset_image",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    
    
    def __str__(self):
        return f"{self.name} - {self.serial_number}"
    
    class Meta: 
        verbose_name = "Asset"
        verbose_name_plural = "Assets"