from rest_framework.serializers import ModelSerializer
from .models import Help, WorldCountry


class HelpSerializer(ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'


class WorldCountrySerializer(ModelSerializer):
    class Meta:
        model = WorldCountry
        fields = ('name', )

