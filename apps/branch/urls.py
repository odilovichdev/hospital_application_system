from django.urls import path

from apps.branch.api import (
    BranchCreateAPIView,
    BranchDirectionCreateAPIView,
    BranchDirectionListAPIView,
    BranchEquipmentCreateAPIView,
    BranchEquipmentListAPIView,
    BranchListAPIView,
    BranchUserAssignAPIVIew,
    BranchUserListAPIView,
)

app_name = "branch"

urlpatterns = [
    path("add/<int:application_id>",
         BranchCreateAPIView.as_view(), name="branch_create"),
    path("<int:application_id>",
         BranchListAPIView.as_view(), name="branch_list"),

    path("<int:branch_id>/add-direction",
         BranchDirectionCreateAPIView.as_view(), name="branch_direction_create"),

    path('<int:branch_direction_id>/add-equipment',
         BranchEquipmentCreateAPIView.as_view(), name='branch_equipment_create'),
    path('<int:branch_direction_id>/equipments',
         BranchEquipmentListAPIView.as_view(), name='branch_equipment_list'),

    path('<int:branch_id>/directions/',
         BranchDirectionListAPIView.as_view(), name='branch-directions'),


    path('<int:branch_direction_id>/assign-user',
         BranchUserAssignAPIVIew.as_view(), name='branch-assign-user'),
    path('<int:branch_direction_id>/users',
         BranchUserListAPIView.as_view(), name='branch-user-list')


]
