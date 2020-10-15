from rest_framework.serializers import ModelSerializer
from .models import City, Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', )


class CitySerializer(ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('name', 'country', )
