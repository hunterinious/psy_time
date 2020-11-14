from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
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
    PsyRandomProfileSerializer,
    PsyPublicProfileSerializer,
    PsyExtendedPublicProfileSerializer,
    PsyStatusSerializer,
    PsyFormatSerializer,
    PsyThemeSerializer,
    PsyApproachSerializer,
    PsySpecializationSerializer,
    PsyEducationSerializer,
    PsySecondaryEducationSerializer,
    PsyLanguageSerializer,
    PsyReviewSerializer,
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
        statuses = PsychologistStatus.objects.get_all()
        formats = PsychologistWorkFormat.objects.get_all()
        themes = PsychologistTheme.objects.get_all()
        approaches = PsychologistApproach.objects.get_all()
        specializations = PsychologistSpecialization.objects.get_all()
        educations = PsychologistEducation.objects.get_all()
        secondary_educations = PsychologistSecondaryEducation.objects.get_all()
        languages = PsychologistLanguage.objects.get_all()

        data = dict()

        data['ages'] = []
        min_age = PsychologistUserProfile.objects.get_min_age()
        max_age = PsychologistUserProfile.objects.get_max_age()
        data['ages'].append({'name': f'{min_age}-{max_age}'})

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


class RandomPsyProfileView(RetrieveAPIView):
    serializer_class = PsyRandomProfileSerializer
    authentication_classes = []
    permission_classes = []

    def get_object(self):
        return PsychologistUserProfile.objects.get_random_profile()


class PsyPublicProfileView(RetrieveAPIView):
    queryset = PsychologistUserProfile.objects.get_profiles()
    serializer_class = PsyPublicProfileSerializer
    authentication_classes = []
    permission_classes = []


class PsyExtendedPublicProfileView(RetrieveAPIView):
    queryset = PsychologistUserProfile.objects.get_profiles()
    serializer_class = PsyExtendedPublicProfileSerializer
    authentication_classes = []
    permission_classes = []


class PsyReviewListView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        if not pk:
            raise AttributeError("View %s must be called with "
                                 "either an object pk."
                                 % self.__class__.__name__)
        try:
            profile = PsychologistUserProfile.objects.get_profile_by_id(id=pk)
        except ObjectDoesNotExist:
            raise Http404("Object with the given pk not found")

        reviews = PsychologistUserProfile.objects.get_reviews(profile)
        data = dict()
        data['reviews'] = PsyReviewSerializer(reviews, many=True).data

        return Response(data)


class HowToChoosePsyView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        with open('static/files/how_to_choose_psychologist.txt', 'r') as file:
            text = file.read()
        return Response(text, content_type='text')
