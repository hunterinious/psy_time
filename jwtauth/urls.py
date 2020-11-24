from django.urls import path
from .views import (
    MyTokenObtainPairView,
    MyTokenRefreshView,
    RegistrationView,
    LoginDataView
)


urlpatterns = [
    path("api-registration/", RegistrationView.as_view(), name="api-registration"),
    path("api-login/", MyTokenObtainPairView.as_view(), name='api-login'),
    path("refresh/", MyTokenRefreshView.as_view(), name='refresh-token'),
    path("login-data/", LoginDataView.as_view(), name='login-data')
]