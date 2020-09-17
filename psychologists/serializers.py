from rest_framework import serializers
from users.serializers import UsernameSerializer
from django.contrib.auth import get_user_model
from psychologists.models import (
    PsychologistUserProfile,
    PsychologistStatus,
)

User = get_user_model()


class PsyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologistStatus
        fields = ('name', )


class PsyProfileForListSerializer(serializers.ModelSerializer):
    user = UsernameSerializer()
    statuses = PsyStatusSerializer(many=True)

    class Meta:
        model = PsychologistUserProfile
        fields = ('user', 'statuses', 'avatar', 'id')


