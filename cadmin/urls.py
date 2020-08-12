from django.urls import path
from .views import (
    UserCreateView,
    PsychologistProfileCreateView,
    PsychologistStatusCreateView,
    PsychologistSpecializationCreateView,
    CountryCreateView,
    CityCreateView,
)


urlpatterns = [
    path("users/create", UserCreateView.as_view(), name='user-create'),
    path("users/profiles/create_psy_profile", PsychologistProfileCreateView.as_view(), name='psy-profile-create'),
    path("psychologists/statuses/create", PsychologistStatusCreateView.as_view(), name='psy-status-create'),
    path("psychologists/specializations/create", PsychologistSpecializationCreateView.as_view(),
         name='psy-specialization-create'),
    path("countries/create", CountryCreateView.as_view(), name='country-create'),
    path("cities/create", CityCreateView.as_view(), name='city-create'),
]
