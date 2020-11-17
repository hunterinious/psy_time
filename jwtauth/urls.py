from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, RegistrationView, LoginDataView


urlpatterns = [
    path("api-registration/", RegistrationView.as_view(), name="registration"),
    path("api-login/", MyTokenObtainPairView.as_view(), name='login'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh-token'),
    path("login-data/", LoginDataView.as_view(), name='login-data')
]