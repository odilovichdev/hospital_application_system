from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id',"fullname", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("fullname", "email")
    readonly_fields = ("user", "application_number", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

