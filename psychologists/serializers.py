from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField, ModelSerializer, Serializer
from django.contrib.auth import get_user_model
from psychologists.models import (
    PsychologistUserProfile,
    PsychologistStatus,
    PsychologistWorkFormat,
    PsychologistTheme,
    PsychologistApproach,
    PsychologistSpecialization,
    PsychologistEducation,
    PsychologistSecondaryEducation,
    PsychologistLanguage,
)

User = get_user_model()


class PsyStatusSerializer(ModelSerializer):
    class Meta:
        model = PsychologistStatus
        fields = ('name', )


class PsyFormatSerializer(ModelSerializer):
    class Meta:
        model = PsychologistWorkFormat
        fields = ('name',)


class PsyThemeSerializer(ModelSerializer):
    class Meta:
        model = PsychologistTheme
        fields = ('name',)


class PsyApproachSerializer(ModelSerializer):
    class Meta:
        model = PsychologistApproach
        fields = ('name',)


class PsySpecializationSerializer(ModelSerializer):
    class Meta:
        model = PsychologistSpecialization
        fields = ('name',)


class PsyEducationSerializer(ModelSerializer):
    class Meta:
        model = PsychologistEducation
        fields = ('name',)


class PsySecondaryEducationSerializer(ModelSerializer):
    class Meta:
        model = PsychologistSecondaryEducation
        fields = ('name',)


class PsyLanguageSerializer(ModelSerializer):
    class Meta:
        model = PsychologistLanguage
        fields = ('name',)


class PsyProfileForListSerializer(ModelSerializer):
    # user = UsernameSerializer()
    username = SerializerMethodField()
    statuses = PsyStatusSerializer(many=True)

    class Meta:
        model = PsychologistUserProfile
        fields = ('username', 'statuses', 'avatar', 'id')

    def get_username(self, obj):
        return obj.user.username
