from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Direction(BaseModel):
    name = models.CharField(_("Direction name"), max_length=255, unique=True)
    description = models.TextField(_("Direction description"))

    class Meta:
        verbose_name = "Direction"
        verbose_name_plural = "Directions"

    def __str__(self):
        return self.name
