from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import WorldCountry
from .serializers import HelpSerializer, WorldCountrySerializer


class WorldCountryListView(ListAPIView):
    queryset = WorldCountry.objects.get_countries()
    pagination_class = None
    serializer_class = WorldCountrySerializer
    authentication_classes = []
    permission_classes = []


class HelpCreateView(generics.CreateAPIView):
    serializer_class = HelpSerializer
    authentication_classes = []
    permission_classes = []
