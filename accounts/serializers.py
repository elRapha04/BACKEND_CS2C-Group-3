from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=False, allow_blank=True, allow_null=True)  # Make phone_number optional

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "phone_number", "password")
        extra_kwargs = {
            "password": {"write_only": True}  # Ensure password is not exposed in responses
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)  # Remove password from validated_data
        user = User(**validated_data)  # Create user without password field
        if password:
            user.set_password(password)  # Hash password properly
        user.save()
        return user

