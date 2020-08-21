from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    LoginView,
    logout_view,
    UserCreateView,
    UserDeleteView,
    PsychologistUserAndProfileCreateView,
    PsychologistUserAndProfileUpdateView,
    PsychologistUserListView,
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
    path("login", LoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
    path("users/create", UserCreateView.as_view(), name='user-create'),
    path("users/<int:id>/delete", UserDeleteView.as_view(), name='user-delete'),
    path("psychologists_profiles/create", PsychologistUserAndProfileCreateView.as_view(),
         name='psy-user-profile-create'),
    path("psychologists_profiles/<int:id>/update", PsychologistUserAndProfileUpdateView.as_view(),
         name='psy-user-profile-update'),
    path("psychologists", PsychologistUserListView.as_view(), name='psy-list'),
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
