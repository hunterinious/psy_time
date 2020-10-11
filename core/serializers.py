from rest_framework.serializers import ModelSerializer
from .models import Help


class HelpSerializer(ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'

