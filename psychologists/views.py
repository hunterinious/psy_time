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

        ages = params.get('ages', None).replace(' ', '')
        if ages:
            ages = ages.strip().split(',')
            for i, v in enumerate(ages):
                ages[i] = int(v)

        genders = params.get('genders', None).replace(' ', '')
        if genders:
            genders = genders.strip().split(',')

        statuses = params.get('statuses', None).replace(' ', '')
        if statuses:
            statuses = statuses.strip().split(',')

        formats = params.get('formats', None).replace(' ', '')
        if formats:
            formats = formats.strip().split(',')

        themes = params.get('themes', None).replace(' ', '')
        if themes:
            themes = themes.strip().split(',')

        approaches = params.get('approaches', None).replace(' ', '')
        if approaches:
            approaches = approaches.strip().split(',')

        specializations = params.get('specializations', None).replace(' ', '')
        if specializations:
            specializations = specializations.strip().split(',')

        educations = params.get('educations', None).replace(' ', '')
        if educations:
            educations = educations.strip().split(',')

        secondary_educations = params.get('secondary_educations', None).replace(' ', '')
        if secondary_educations:
            secondary_educations = secondary_educations.strip().split(',')

        languages = params.get('languages', None).replace(' ', '')
        if languages:
            languages = languages.strip().split(',')

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


