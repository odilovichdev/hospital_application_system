from django.contrib import admin

from .models import Branch, BranchDirection, BranchEquipment, BranchUser


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id','name','application','description')



@admin.register(BranchUser)
class BranchUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'branch_direction',
    )


@admin.register(BranchDirection)
class BranchDirectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'branch',
        'direction',
    )


@admin.register(BranchEquipment)
class BranchEquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'equipment',
        'branch_direction',
    )

