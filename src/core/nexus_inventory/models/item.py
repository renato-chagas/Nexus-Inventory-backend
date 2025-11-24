from django.db import models

from .category import Category
from .employee import Employee

class Item(models.Model):
    name = models.CharField(max_length=100)
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    person_in_charge = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.serial_number}"
    
    class Meta: 
        verbose_name = "Item"
        verbose_name_plural = "Items"