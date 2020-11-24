from rest_framework_simplejwt.serializers import (
 TokenObtainPairSerializer,
 TokenRefreshSerializer
)
from .utils import get_refresh_expire


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['refresh_expire'] = get_refresh_expire()
        return data


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['refresh_expire'] = get_refresh_expire()
        return data
