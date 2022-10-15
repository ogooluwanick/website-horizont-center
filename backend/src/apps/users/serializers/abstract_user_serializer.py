from rest_framework import serializers
from apps.users.models import User


class AbstractUserSerializer(serializers.ModelSerializer):
    profile: serializers.ModelSerializer

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'phone_number',
            'second_phone_number', 'profile',
        )
