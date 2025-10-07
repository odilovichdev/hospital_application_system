from django.contrib import admin

from .models import Direction


@admin.register(Direction)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
