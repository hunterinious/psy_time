from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        time = datetime.now()
        data['refresh_expired'] = time + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
        return data
