from rest_framework.serializers import SerializerMethodField, ModelSerializer
from django.urls import reverse
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


class CityDynamicSerializer(ModelSerializer):
    data_url = SerializerMethodField()
    delete_url = SerializerMethodField()

    class Meta:
        model = City
        fields = ('id', 'name', 'data_url', 'delete_url')

    def get_data_url(self, obj):
        return reverse('city-update-dynamic', kwargs={'pk': obj.id})

    def get_delete_url(self, obj):
        return reverse('city-delete-dynamic', kwargs={'pk': obj.id})
