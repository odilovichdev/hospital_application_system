from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Equipment(BaseModel):
    name = models.CharField(_("Equipment name"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"

    def __str__(self):
        return self.name
