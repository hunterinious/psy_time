from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import (
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
from .serializers import (
    PsyProfileForListSerializer,
    PsyStatusSerializer,
    PsyFormatSerializer,
    PsyThemeSerializer,
    PsyApproachSerializer,
    PsySpecializationSerializer,
    PsyEducationSerializer,
    PsySecondaryEducationSerializer,
    PsyLanguageSerializer,
)


class PsyProfileListView(ListAPIView):
    queryset = PsychologistUserProfile.objects.all()
    serializer_class = PsyProfileForListSerializer
    permission_classes = []


class PsyProfileFilterCriteriaView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        ages = PsychologistUserProfile.get_ages()
        genders = PsychologistUserProfile.Gender.get_genders()
        statuses = PsychologistStatus.get_statuses()
        formats = PsychologistWorkFormat.get_formats()
        themes = PsychologistTheme.get_themes()
        approaches = PsychologistApproach.get_approaches()
        specializations = PsychologistSpecialization.get_specializations()
        educations = PsychologistEducation.get_educations()
        secondary_educations = PsychologistSecondaryEducation.get_secondary_educations()
        languages = PsychologistLanguage.get_languages()

        data = dict()

        data['ages'] = ages
        data['genders'] = genders
        data['statuses'] = PsyStatusSerializer(statuses, many=True).data
        data['formats'] = PsyFormatSerializer(formats, many=True).data
        data['themes'] = PsyThemeSerializer(themes, many=True).data
        data['approaches'] = PsyApproachSerializer(approaches, many=True).data
        data['specializations'] = PsySpecializationSerializer(specializations, many=True).data
        data['educations'] = PsyEducationSerializer(educations, many=True).data
        data['secondary_educations'] = PsySecondaryEducationSerializer(secondary_educations, many=True).data
        data['languages'] = PsyLanguageSerializer(languages, many=True).data

        return Response(data)
