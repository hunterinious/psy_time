from rest_framework.serializers import SerializerMethodField, ModelSerializer
from locations.serializers import CitySerializer
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
    PsychologistReview,
)
from datetime import date

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


class PsyReviewSerializer(ModelSerializer):
    username = SerializerMethodField()

    class Meta:
        model = PsychologistReview
        fields = ('username', 'text')

    def get_username(self, obj):
        return obj.author_profile.user.username


class PsyProfileForListSerializer(ModelSerializer):
    username = SerializerMethodField()
    statuses = PsyStatusSerializer(many=True)

    class Meta:
        model = PsychologistUserProfile
        fields = ('username', 'statuses', 'avatar', 'id')

    def get_username(self, obj):
        return obj.user.username


class PsyRandomProfileSerializer(ModelSerializer):
    username = SerializerMethodField()

    class Meta:
        model = PsychologistUserProfile
        fields = ('username', 'avatar', 'id')

    def get_username(self, obj):
        return obj.user.username


class PsyPublicProfileSerializer(ModelSerializer):
    username = SerializerMethodField()
    reviews_count = SerializerMethodField()

    class Meta:
        model = PsychologistUserProfile
        fields = ('username', 'avatar', 'id', 'about', 'duration', 'price', 'reviews_count')

    def get_username(self, obj):
        return obj.user.username

    def get_reviews_count(self, obj):
        return PsychologistUserProfile.objects.get_reviews_count(obj.id)


class PsyExtendedPublicProfileSerializer(ModelSerializer):
    city = CitySerializer()
    age = SerializerMethodField()
    statuses = PsyStatusSerializer(many=True)
    formats = PsyFormatSerializer(many=True)
    themes = PsyThemeSerializer(many=True)
    approaches = PsyApproachSerializer(many=True)
    specializations = PsySpecializationSerializer(many=True)
    educations = PsyEducationSerializer(many=True)
    secondary_educations = PsySecondaryEducationSerializer(many=True)
    languages = PsyLanguageSerializer(many=True)

    class Meta:
        model = PsychologistUserProfile
        exclude = ('user', 'avatar', 'id', 'about', 'duration', 'price', 'gender', 'birth_date')

    def get_age(self, obj):
        current_year = date.today().year
        birth_year = obj.birth_date.year
        return current_year - birth_year
