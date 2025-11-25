from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tracks_software = models.BooleanField(default=False, help_text="Indicates if items in this category require software tracking.")
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
        