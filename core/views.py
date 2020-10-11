from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelpSerializer
import json


class WorldCountriesListView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        with open('static/files/countries.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return Response(data)


class HelpView(generics.CreateAPIView):
    serializer_class = HelpSerializer
    authentication_classes = []
    permission_classes = []

