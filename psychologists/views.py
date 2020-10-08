from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
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


class PsyProfileForListPagination(PageNumberPagination):
    page_size = 20
    page_query_description = 'size'
    max_page_size = 28


class PsyProfileListView(ListAPIView):
    queryset = PsychologistUserProfile.objects.all()
    pagination_class = PsyProfileForListPagination
    serializer_class = PsyProfileForListSerializer
    authentication_classes = []
    permission_classes = []


class PsyProfileFilteredListView(ListAPIView):
    pagination_class = PsyProfileForListPagination
    serializer_class = PsyProfileForListSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        params = self.request.query_params

        ages = params.getlist('ages', None)
        if ages:
            for i, v in enumerate(ages):
                ages[i] = int(v)

        genders = params.getlist('genders', None)
        statuses = params.getlist('statuses', None)
        formats = params.getlist('formats', None)
        themes = params.getlist('themes', None)
        approaches = params.getlist('approaches', None)
        specializations = params.getlist('specializations', None)
        educations = params.getlist('educations', None)
        secondary_educations = params.getlist('secondary_educations', None)
        languages = params.getlist('languages', None)

        return PsychologistUserProfile.objects.\
            get_profiles_by_criteria(ages, genders, statuses, formats, themes, approaches, specializations,
                                     educations, secondary_educations, languages)


class PsyProfileCriteriaView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        genders = PsychologistUserProfile.objects.get_genders()
        statuses = PsychologistStatus.objects.get_statuses()
        formats = PsychologistWorkFormat.objects.get_formats()
        themes = PsychologistTheme.objects.get_themes()
        approaches = PsychologistApproach.objects.get_approaches()
        specializations = PsychologistSpecialization.objects.get_specializations()
        educations = PsychologistEducation.objects.get_educations()
        secondary_educations = PsychologistSecondaryEducation.objects.get_secondary_educations()
        languages = PsychologistLanguage.objects.get_languages()

        data = dict()

        data['ages'] = []
        data['ages'].append({'name': '18-100'})

        data['genders'] = []
        for gender in genders:
            data['genders'].append({'name': gender})

        data['statuses'] = PsyStatusSerializer(statuses, many=True).data
        data['formats'] = PsyFormatSerializer(formats, many=True).data
        data['themes'] = PsyThemeSerializer(themes, many=True).data
        data['approaches'] = PsyApproachSerializer(approaches, many=True).data
        data['specializations'] = PsySpecializationSerializer(specializations, many=True).data
        data['educations'] = PsyEducationSerializer(educations, many=True).data
        data['secondary_educations'] = PsySecondaryEducationSerializer(secondary_educations, many=True).data
        data['languages'] = PsyLanguageSerializer(languages, many=True).data

        return Response(data)


class HowToChoosePsychologistView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        with open('static/files/how_to_choose_psychologist.txt', 'r') as file:
            text = file.read()
        return Response(text, content_type='text')


