from typing import ClassVar

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..common.models import BaseModel
from .managers import UserManager


class Users(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_("Email"), unique=True)
    fullname = models.CharField(_("Fullname"), null=True, blank=True)
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is Superuser"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: ClassVar[list[str]] = ["fullname"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.email}"


class Employee(BaseModel):
    email = models.EmailField(_("Email"), unique=True)
    fullname = models.CharField(_("Fullname"), null=True, blank=True)

    user = models.ForeignKey(
        'Users', on_delete=models.CASCADE, related_name='employees'
    )

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")


    def __str__(self):
        return f"{self.fullname}"


