from rest_framework import generics
from .serializers import HelpSerializer


class HelpCreateView(generics.CreateAPIView):
    serializer_class = HelpSerializer
    authentication_classes = []
    permission_classes = []
