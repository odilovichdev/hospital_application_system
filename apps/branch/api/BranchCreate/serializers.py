from rest_framework import serializers

from apps.applications.models import Application
from apps.branch.models import Branch


class BranchApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'application_number')


class BranchCreateSerializer(serializers.ModelSerializer):
    application = BranchApplicationSerializer(read_only=True)
    class Meta:
        model = Branch
        fields = (
            'id',
            'name',
            'description',
            'application',
        )
        read_only_fields = ('id', 'application')



    def validate(self, data):
        request = self.context.get('request')
        app = self.context.get('app')

        if app.user != request.user:
            raise serializers.ValidationError('"Siz bu application uchun branch yarata olmaysiz."')

        return data