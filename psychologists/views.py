from rest_framework.generics import ListAPIView
from .models import PsychologistUserProfile
from .serializers import PsyProfileForListSerializer


class PsyProfileListView(ListAPIView):
    queryset = PsychologistUserProfile.objects.all()
    serializer_class = PsyProfileForListSerializer
    permission_classes = []