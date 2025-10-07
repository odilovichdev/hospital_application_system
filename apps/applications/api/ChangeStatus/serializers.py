from typing import ClassVar

from django.core.mail import send_mail
from rest_framework import serializers

from apps.applications.models import Application


class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields: ClassVar[list[str]] = ["status"]

    def validate_status(self, new_status):
        instance = self.instance
        current_status = instance.status

        allowed_transitions = {
            "draft": ["submitted"],
            "submitted": ["review"],
            "review": ["approved", "rejected"],
            "approved": [],
            "rejected": [],
        }

        if new_status not in allowed_transitions.get(current_status, []):
            raise serializers.ValidationError(
                f"{current_status.upper()} holatidan {new_status.upper()} holatiga o‘tish mumkin emas."
            )

        if new_status == "submitted" and not instance.can_submit():
            raise serializers.ValidationError("Ariza to‘liq to‘ldirilmagan, yuborish mumkin emas.")

        request = self.context.get("request")
        if current_status == "submitted" and new_status == "review" and not request.user.is_staff:
            raise serializers.ValidationError("Faqat admin review bosqichiga o‘tkazishi mumkin.")

        if current_status == "review" and new_status in ["approved", "rejected"] and not request.user.is_staff:
            raise serializers.ValidationError("Faqat admin approved/rejected ga o‘tkazishi mumkin.")

        return new_status

    def update(self, instance, validated_data):
        old_status = instance.status
        new_status = validated_data.get("status")

        instance.status = new_status

        if old_status == "draft" and new_status == "submitted":
            if not instance.registration_number:
                instance.registration_number = instance.generate_registration_number()

            send_mail(
                subject="Sizning arizangiz yuborildi",
                message=f"Sizning {instance.application_number} raqamli arizangiz qabul qilindi.\n"
                        f"Ro‘yxatga olish raqami: {instance.registration_number}.",
                from_email="fazliddinn.gadoyev@gmail.com",
                recipient_list=[instance.email],
                fail_silently=True,
            )

        instance.save()
        return instance
