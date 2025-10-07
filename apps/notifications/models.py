from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Notification(BaseModel):
    class ViaType(models.TextChoices):
        EMAIL = "email", "Email"
        SMS = "sms", "SMS"

    application = models.ForeignKey(
        'applications.Application',
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    message = models.CharField(_("Message"), max_length=500)
    via_type = models.CharField(_("Via type"), max_length=20, choices=ViaType.choices)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.via_type} - {self.application.application_number}"

