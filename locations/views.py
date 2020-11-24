from rest_framework.generics import ListAPIView
from .models import Country
from .serializers import CountrySerializer


class CountryListView(ListAPIView):
    queryset = Country.objects.get_all()
    pagination_class = None
    serializer_class = CountrySerializer
    authentication_classes = []
    permission_classes = []

