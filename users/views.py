from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import RegularUserProfile
from .serializers import (
    RegularUserProfileRetrieveSerializer,
    RegularUserForUpdateProfileSerializer,
)

user = get_user_model()


class RegularUserAndProfileView(RetrieveUpdateAPIView):
    queryset = RegularUserProfile.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        object = super(RegularUserAndProfileView, self).get_object()
        if self.request.method == 'GET':
            return object
        elif self.request.method == 'PATCH':
            return object.user

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RegularUserProfileRetrieveSerializer
        elif self.request.method == 'PATCH':
            return RegularUserForUpdateProfileSerializer
