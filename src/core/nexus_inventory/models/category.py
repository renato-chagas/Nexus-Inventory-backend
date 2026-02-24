from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tracks_software = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    @property
    def quantity(self):
        return self.asset_set.count()

    def __str__(self):
        return f"{self.name} ({self.quantity})"

    class Meta:
        verbose_name = "Category"
