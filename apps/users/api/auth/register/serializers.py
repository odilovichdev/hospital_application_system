from rest_framework import serializers

from apps.users.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'password', 'fullname')


    def validate_email(self, email):
        if '@' not in email:
            raise serializers.ValidationError({"email": "Invalid email!"})

        user = Users.objects.filter(email=email).first()

        if user:
            raise serializers.ValidationError({"detail": "User already exists!"})

        return email

    def validate_password(self, password):
        if len(password) < 4:
            raise serializers.ValidationError({"password": "Password must be at least 4 characters!"})

        return password

    def create(self, validated_data):
        user = Users.objects.create(
            email=validated_data['email'],
            fullname=validated_data['fullname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




