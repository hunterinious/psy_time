from rest_framework.serializers import SerializerMethodField, ModelSerializer
from locations.serializers import CitySerializer
from django.contrib.auth import get_user_model
from django.urls import reverse
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
from users.models import PsychologistUser
from datetime import date

User = get_user_model()


class PsyStatusSerializer(ModelSerializer):
    class Meta:
        model = PsychologistStatus
        fields = ('name', )


class PsyStatusDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistStatus
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-status-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-status-delete-dynamic', kwargs={'pk': obj.id})


class PsyFormatSerializer(ModelSerializer):
    class Meta:
        model = PsychologistWorkFormat
        fields = ('name',)


class PsyFormatDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistWorkFormat
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-format-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-format-delete-dynamic', kwargs={'pk': obj.id})


class PsyThemeSerializer(ModelSerializer):
    class Meta:
        model = PsychologistTheme
        fields = ('name',)


class PsyThemeDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistTheme
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-theme-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-theme-delete-dynamic', kwargs={'pk': obj.id})


class PsyApproachSerializer(ModelSerializer):
    class Meta:
        model = PsychologistApproach
        fields = ('name',)


class PsyApproachDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistWorkFormat
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-approach-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-approach-delete-dynamic', kwargs={'pk': obj.id})


class PsySpecializationSerializer(ModelSerializer):
    class Meta:
        model = PsychologistSpecialization
        fields = ('name',)


class PsySpecializationDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistWorkFormat
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-specialization-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-specialization-delete-dynamic', kwargs={'pk': obj.id})


class PsyEducationSerializer(ModelSerializer):
    class Meta:
        model = PsychologistEducation
        fields = ('name',)


class PsyEducationDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistWorkFormat
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-education-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-education-delete-dynamic', kwargs={'pk': obj.id})


class PsySecondaryEducationSerializer(ModelSerializer):
    class Meta:
        model = PsychologistSecondaryEducation
        fields = ('name',)


class PsySecondaryEducationDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistWorkFormat
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-secondary-education-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-secondary-education-delete-dynamic', kwargs={'pk': obj.id})


class PsyLanguageSerializer(ModelSerializer):
    class Meta:
        model = PsychologistLanguage
        fields = ('name',)


class PsyLanguageDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = PsychologistWorkFormat
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('psy-language-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('psy-language-delete-dynamic', kwargs={'pk': obj.id})


class PsyReviewSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()

    class Meta:
        model = PsychologistReview
        fields = ('first_name', 'last_name', 'text')

    def get_first_name(self, obj):
        return obj.author.first_name

    def get_last_name(self, obj):
        return obj.author.last_name


class PsyProfileForListSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    statuses = PsyStatusSerializer(many=True)

    class Meta:
        model = PsychologistUserProfile
        fields = ('first_name', 'last_name', 'statuses', 'avatar', 'id')

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name


class PsyRandomProfileSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()

    class Meta:
        model = PsychologistUserProfile
        fields = ('first_name', 'last_name', 'avatar', 'id')

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name


class PsyPublicProfileSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    reviews_count = SerializerMethodField()

    class Meta:
        model = PsychologistUserProfile
        fields = ('first_name', 'last_name', 'avatar', 'id', 'about', 'duration', 'price', 'reviews_count')

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_reviews_count(self, obj):
        profile = PsychologistUserProfile.objects.get_profile_by_id(obj.id)
        return PsychologistUser.objects.get_reviews_count(profile.user)


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
