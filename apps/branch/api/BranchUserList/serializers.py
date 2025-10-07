from rest_framework import serializers

from apps.branch.models import BranchUser
from apps.users.models import Users


class BranchUserUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'fullname', 'email')


class BranchUserListSerializer(serializers.ModelSerializer):
    user = BranchUserUserSerializer()

    class Meta:
        model = BranchUser
        fields = ('id', 'user')
