from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    hire_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def auto_date():
        if hire_date == None:
            hire_date = timezone.now()
            
    class Meta: 
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    
    
    