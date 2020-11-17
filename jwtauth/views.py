from django.conf import settings
from rest_framework import response, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from users.serializers import RegularUserCreateSerializer, UserLoginDataSerializer
from rest_framework.views import APIView
from datetime import datetime


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegistrationView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegularUserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        time = datetime.now()
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            'refresh_expired': time + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
        }
        return response.Response(res, status.HTTP_201_CREATED)


class LoginDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = UserLoginDataSerializer(request.user).data
        return response.Response(data)

