from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    class Meta:
        abstract = True
