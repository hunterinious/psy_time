from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import PsychologistUserProfile
from .serializers import PsyProfileForListSerializer


class PsyProfileForListPagination(PageNumberPagination):
    page_size = 20
    page_query_description = 'size'
    max_page_size = 28


class PsyProfileListView(ListAPIView):
    queryset = PsychologistUserProfile.objects.all()
    serializer_class = PsyProfileForListSerializer
    pagination_class = PsyProfileForListPagination
    permission_classes = []