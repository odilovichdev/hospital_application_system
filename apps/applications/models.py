from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

User = get_user_model()


class Application(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SUBMITTED = "submitted", "Submitted"
        REVIEW = "review", "Review"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    application_number = models.CharField(
        _("Application number"), max_length=50, unique=True
    )
    fullname = models.CharField(_("Full name"), max_length=255)
    phone_number = models.CharField(_("Phone number"), max_length=20)
    email = models.EmailField(_("Email"), max_length=255)
    file = models.FileField(_("Attached file"), upload_to="applications/", null=True, blank=True)
    status = models.CharField(
        _("Status"), max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    registration_number = models.CharField(
        _("Registration number"), max_length=50, null=True, blank=True, unique=True
    )
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )

    def save(self, *args, **kwargs):
        if not self.application_number:
            last_application = Application.objects.order_by('id').last()
            if last_application:
                last_id = int(last_application.application_number.split('-')[-1])
                new_id = last_id + 1
            else:
                new_id = 1
            self.application_number = f"APP-{new_id:05d}"
        return super().save(*args, **kwargs)

    def generate_registration_number(self):
        last = Application.objects.exclude(registration_number=None).order_by("id").last()
        next_id = 1 if not last else int(last.registration_number.split("-")[-1]) + 1
        return f"REG-{next_id:05d}"


    def can_submit(self):
        """Check if the application can be submitted"""
        required_fields = [self.fullname, self.phone_number, self.email]
        return all(required_fields) and self.has_all_required_relations()

    def has_all_required_relations(self):
        """Tekshiradi: har bir branchda kamida 1 ta direction, user va equipment mavjudmi"""
        for branch in self.branches.all():
            if not branch.branch_directions.exists():
                return False
            for bd in branch.branch_directions.all():
                if not bd.branch_users.exists():
                    return False
                if not bd.branch_equipments.exists():
                    return False
        return True

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"

    def __str__(self):
        return f"{self.fullname} ({self.application_number})"



