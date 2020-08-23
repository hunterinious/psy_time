from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    MainAdminView,
    UserCreateView,
    UserDeleteView,
    PsychologistUserAndProfileCreateView,
    PsychologistUserAndProfileUpdateView,
    PsychologistUserListView,
    PsychologistStatusListView,
    PsychologistStatusCreateView,
    PsychologistApproachListView,
    PsychologistApproachCreateView,
    PsychologistSpecializationListView,
    PsychologistSpecializationCreateView,
    PsychologistFormatListView,
    PsychologistFormatCreateView,
    PsychologistThemeListView,
    PsychologistThemeCreateView,
    PsychologistEducationListView,
    PsychologistEducationCreateView,
    PsychologistSecondaryEducationListView,
    PsychologistSecondaryEducationCreateView,
    PsychologistLanguageListView,
    PsychologistLanguageCreateView,
    CountryListView,
    CountryCreateView,
    CityListView,
    CityCreateView,
)


urlpatterns = [
    path("", MainAdminView.as_view(), name="admin-main"),

    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),

    path("users/create", UserCreateView.as_view(), name='user-create'),
    path("users/<int:id>/delete", UserDeleteView.as_view(), name='user-delete'),

    path("psychologists_profiles/create", PsychologistUserAndProfileCreateView.as_view(),
         name='psy-user-profile-create'),
    path("psychologists_profiles/<int:id>/update", PsychologistUserAndProfileUpdateView.as_view(),
         name='psy-user-profile-update'),
    path("psychologists", PsychologistUserListView.as_view(), name='psy-list'),

    path("psychologists/statuses", PsychologistStatusListView.as_view(), name='psy-status-list'),
    path("psychologists/statuses/create", PsychologistStatusCreateView.as_view(), name='psy-status-create'),
    path("psychologists/approaches", PsychologistApproachListView.as_view(), name='psy-approach-list'),
    path("psychologists/approaches/create", PsychologistApproachCreateView.as_view(), name='psy-approach-create'),
    path("psychologists/specializations", PsychologistSpecializationListView.as_view(),
         name='psy-specialization-list'),
    path("psychologists/specializations/create", PsychologistSpecializationCreateView.as_view(),
         name='psy-specialization-create'),
    path("psychologists/formats", PsychologistFormatListView.as_view(), name='psy-format-list'),
    path("psychologists/formats/create", PsychologistFormatCreateView.as_view(), name='psy-format-create'),
    path("psychologists/themes", PsychologistThemeListView.as_view(), name='psy-theme-list'),
    path("psychologists/themes/create", PsychologistThemeCreateView.as_view(), name='psy-theme-create'),
    path("psychologists/educations", PsychologistEducationListView.as_view(), name='psy-education-list'),
    path("psychologists/educations/create", PsychologistEducationCreateView.as_view(), name='psy-education-create'),
    path("psychologists/secondary_educations", PsychologistSecondaryEducationListView.as_view(),
         name='psy-secondary-education-list'),
    path("psychologists/secondary_educations/create", PsychologistSecondaryEducationCreateView.as_view(),
         name='psy-secondary-education-create'),
    path("psychologists/languages", PsychologistLanguageListView.as_view(), name='psy-language-list'),
    path("psychologists/languages/create", PsychologistLanguageCreateView.as_view(), name='psy-language-create'),

    path("countries", CountryListView.as_view(), name='country-list'),
    path("countries/create", CountryCreateView.as_view(), name='country-create'),
    path("cities", CityListView.as_view(), name='city-list'),
    path("cities/create", CityCreateView.as_view(), name='city-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
