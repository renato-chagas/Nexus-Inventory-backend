from django.db import models

from .employee import Employee


class AssetHistory(models.Model):
    action_date = models.DateTimeField(auto_now_add=True)
    ACTION_CHOICES = [
        ("CHECKOUT", "delivered to employee"),
        ("CHECKIN", "returned to inventory"),
        ("MAINTENANCE", "sent for maintenance"),
        ("DISPOSAL", "disposed"),
    ]
    action_type = models.CharField(
        max_length=50, choices=ACTION_CHOICES, default="CHECKOUT"
    )
    observaitions = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset = models.ForeignKey(
        "Asset",
        on_delete=models.CASCADE,
        related_name="asset_history",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Asset History"
        verbose_name_plural = "Asset Histories"
        ordering = ["-action_date"]

    def __str__(self):
        return f"{self.action_type} on {self.action_date} by {self.employee}"
