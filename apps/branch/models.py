from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

User = get_user_model()


class Branch(BaseModel):
    application = models.ForeignKey(
        'applications.Application', on_delete=models.CASCADE, related_name="branches"
    )
    name = models.CharField(_("Branch name"), max_length=255, unique=True)
    description = models.TextField(_("Branch description"))

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return f"{self.application.application_number} - {self.name}"


class BranchDirection(BaseModel):
    branch = models.ForeignKey(
        'Branch', on_delete=models.CASCADE, related_name="branch_directions"
    )
    direction = models.ForeignKey(
        'directions.Direction', on_delete=models.CASCADE, related_name='branch_directions'
    )


    def __str__(self):
        return f"{self.direction.name} - {self.branch.name}"

    class Meta:
        verbose_name = "Branch Direction"
        verbose_name_plural = "Branch Directions"
        unique_together = ('branch', 'direction')


class BranchUser(BaseModel):
    branch_direction = models.ForeignKey(
        'BranchDirection',
        on_delete=models.CASCADE,
        related_name='branch_users'
    )
    user = models.ForeignKey(
        'users.Employee',
        on_delete=models.CASCADE,
        related_name='branch_users'
    )

    class Meta:
        verbose_name = "Branch User"
        verbose_name_plural = "Branch Users"
        unique_together = ('branch_direction', 'user')

    def __str__(self):
        return f"{self.user.fullname} - {self.branch_direction_id}"


class BranchEquipment(BaseModel):
    branch_direction = models.ForeignKey(
        'BranchDirection',
        on_delete=models.CASCADE,
        related_name='branch_equipments'
    )
    equipment = models.ForeignKey(
        'equipments.Equipment',
        on_delete=models.CASCADE,
        related_name='branch_equipments'
    )

    class Meta:
        verbose_name = "Branch equipment"
        verbose_name_plural = "Branch equipments"
        unique_together = ('branch_direction', 'equipment')

    def __str__(self):
        return f"{self.equipment.name} - {self.branch_direction_id}"