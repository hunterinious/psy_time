from django.urls import path
from .views import (
    UserCreateView,
    PsychologistProfileCreateView,
    PsychologistStatusCreateView,
    PsychologistFormatCreateView,
    CountryCreateView,
    CityCreateView,
)


urlpatterns = [
    path("users/create", UserCreateView.as_view(), name='user-create'),
    path("users/profiles/create_psy_profile", PsychologistProfileCreateView.as_view(), name='psy-profile-create'),
    path("psychologists/statuses/create", PsychologistStatusCreateView.as_view(), name='psy-status-create'),
    path("psychologists/formats/create", PsychologistFormatCreateView.as_view(), name='psy-format-create'),
    path("countries/create", CountryCreateView.as_view(), name='country-create'),
    path("cities/create", CityCreateView.as_view(), name='city-create'),
]
