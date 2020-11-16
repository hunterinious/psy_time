from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, RegistrationView


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", MyTokenObtainPairView.as_view(), name='login'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh-token'),
]