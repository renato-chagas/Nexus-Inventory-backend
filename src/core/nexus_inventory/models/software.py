from django.db import models

class Software(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    
    def __str__(self)   :
        return f"{self.name} - {self.version}"
    
    class Meta:
        verbose_name = "Software"
        verbose_name_plural = "Softwares"