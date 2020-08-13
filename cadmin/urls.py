from django.urls import path
from .views import (
    UserCreateView,
    PsychologistProfileCreateView,
    PsychologistStatusCreateView,
    PsychologistApproachCreateView,
    PsychologistSpecializationCreateView,
    PsychologistFormatCreateView,
    PsychologistThemeCreateView,
    PsychologistEducationCreateView,
    PsychologistSecondaryEducationCreateView,
    PsychologistLanguageCreateView,
    CountryCreateView,
    CityCreateView,
)


urlpatterns = [
    path("users/create", UserCreateView.as_view(), name='user-create'),
    path("users/profiles/create_psy_profile", PsychologistProfileCreateView.as_view(), name='psy-profile-create'),
    path("psychologists/statuses/create", PsychologistStatusCreateView.as_view(), name='psy-status-create'),
    path("psychologists/approaches/create", PsychologistApproachCreateView.as_view(), name='psy-approach-create'),
    path("psychologists/specializations/create", PsychologistSpecializationCreateView.as_view(),
         name='psy-specialization-create'),
    path("psychologists/formats/create", PsychologistFormatCreateView.as_view(), name='psy-format-create'),
    path("psychologists/themes/create", PsychologistThemeCreateView.as_view(), name='psy-theme-create'),
    path("psychologists/educations/create", PsychologistEducationCreateView.as_view(), name='psy-education-create'),
    path("psychologists/secondary_educations/create", PsychologistSecondaryEducationCreateView.as_view(),
         name='psy-secondary-education-create'),
    path("psychologists/languages/create", PsychologistLanguageCreateView.as_view(), name='psy-language-create'),
    path("countries/create", CountryCreateView.as_view(), name='country-create'),
    path("cities/create", CityCreateView.as_view(), name='city-create'),
]
