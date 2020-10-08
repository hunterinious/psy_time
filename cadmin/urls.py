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
    PsychologistStatusUpdateView,
    PsychologistStatusDeleteView,
    PsychologistApproachListView,
    PsychologistApproachCreateView,
    PsychologistApproachUpdateView,
    PsychologistApproachDeleteView,
    PsychologistSpecializationListView,
    PsychologistSpecializationCreateView,
    PsychologistSpecializationUpdateView,
    PsychologistSpecializationDeleteView,
    PsychologistFormatListView,
    PsychologistFormatCreateView,
    PsychologistFormatUpdateView,
    PsychologistFormatDeleteView,
    PsychologistThemeListView,
    PsychologistThemeCreateView,
    PsychologistThemeUpdateView,
    PsychologistThemeDeleteView,
    PsychologistEducationListView,
    PsychologistEducationCreateView,
    PsychologistEducationUpdateView,
    PsychologistEducationDeleteView,
    PsychologistSecondaryEducationListView,
    PsychologistSecondaryEducationCreateView,
    PsychologistSecondaryEducationUpdateView,
    PsychologistSecondaryEducationDeleteView,
    PsychologistLanguageListView,
    PsychologistLanguageCreateView,
    PsychologistLanguageUpdateView,
    PsychologistLanguageDeleteView,
    CountryListView,
    CountryCreateView,
    CountryUpdateView,
    CountryDeleteView,
    CityListView,
    CityCreateView,
    CityUpdateView,
    CityDeleteView,
)


urlpatterns = [
    path("", MainAdminView.as_view(), name="admin-main"),

    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),

    path("users/create", UserCreateView.as_view(), name='user-create'),
    path("users/<int:id>/delete", UserDeleteView.as_view(), name='user-delete'),

    path("psychologists-profiles/create", PsychologistUserAndProfileCreateView.as_view(),
         name='psy-user-profile-create'),
    path("psychologists-profiles/<int:id>/update", PsychologistUserAndProfileUpdateView.as_view(),
         name='psy-user-profile-update'),
    path("psychologists", PsychologistUserListView.as_view(), name='psy-list'),

    path("psychologists/statuses", PsychologistStatusListView.as_view(), name='psy-status-list'),
    path("psychologists/statuses/create", PsychologistStatusCreateView.as_view(), name='psy-status-create'),
    path("psychologists/statuses/<int:id>/update", PsychologistStatusUpdateView.as_view(), name='psy-status-update'),
    path("psychologists/statuses/<int:id>/delete", PsychologistStatusDeleteView.as_view(), name='psy-status-delete'),

    path("psychologists/approaches", PsychologistApproachListView.as_view(), name='psy-approach-list'),
    path("psychologists/approaches/create", PsychologistApproachCreateView.as_view(), name='psy-approach-create'),
    path("psychologists/approaches/<int:id>/update", PsychologistApproachUpdateView.as_view(),
         name='psy-approach-update'),
    path("psychologists/approaches/<int:id>/delete", PsychologistApproachDeleteView.as_view(),
         name='psy-approach-delete'),

    path("psychologists/specializations", PsychologistSpecializationListView.as_view(),
         name='psy-specialization-list'),
    path("psychologists/specializations/create", PsychologistSpecializationCreateView.as_view(),
         name='psy-specialization-create'),
    path("psychologists/specializations/<int:id>/update", PsychologistSpecializationUpdateView.as_view(),
         name='psy-specialization-update'),
    path("psychologists/specializations/<int:id>/delete", PsychologistSpecializationDeleteView.as_view(),
         name='psy-specialization-delete'),


    path("psychologists/formats", PsychologistFormatListView.as_view(), name='psy-format-list'),
    path("psychologists/formats/create", PsychologistFormatCreateView.as_view(), name='psy-format-create'),
    path("psychologists/formats/<int:id>/update", PsychologistFormatUpdateView.as_view(), name='psy-format-update'),
    path("psychologists/formats/<int:id>/delete", PsychologistFormatDeleteView.as_view(), name='psy-format-delete'),

    path("psychologists/themes", PsychologistThemeListView.as_view(), name='psy-theme-list'),
    path("psychologists/themes/create", PsychologistThemeCreateView.as_view(), name='psy-theme-create'),
    path("psychologists/themes/<int:id>/update", PsychologistThemeUpdateView.as_view(), name='psy-theme-update'),
    path("psychologists/themes/<int:id>/delete", PsychologistThemeDeleteView.as_view(), name='psy-theme-delete'),

    path("psychologists/educations", PsychologistEducationListView.as_view(), name='psy-education-list'),
    path("psychologists/educations/create", PsychologistEducationCreateView.as_view(), name='psy-education-create'),
    path("psychologists/educations/<int:id>/update", PsychologistEducationUpdateView.as_view(),
         name='psy-education-update'),
    path("psychologists/educations/<int:id>/delete", PsychologistEducationDeleteView.as_view(),
         name='psy-education-delete'),


    path("psychologists/secondary-educations", PsychologistSecondaryEducationListView.as_view(),
         name='psy-secondary-education-list'),
    path("psychologists/secondary-educations/create", PsychologistSecondaryEducationCreateView.as_view(),
         name='psy-secondary-education-create'),
    path("psychologists/secondary-educations/<int:id>/update", PsychologistSecondaryEducationUpdateView.as_view(),
         name='psy-secondary-education-update'),
    path("psychologists/secondary-educations/<int:id>/delete", PsychologistSecondaryEducationDeleteView.as_view(),
         name='psy-secondary-education-delete'),

    path("psychologists/languages", PsychologistLanguageListView.as_view(), name='psy-language-list'),
    path("psychologists/languages/create", PsychologistLanguageCreateView.as_view(), name='psy-language-create'),
    path("psychologists/languages/<int:id>/update", PsychologistLanguageUpdateView.as_view(),
         name='psy-language-update'),
    path("psychologists/languages/<int:id>/delete", PsychologistLanguageDeleteView.as_view(),
         name='psy-language-delete'),

    path("countries", CountryListView.as_view(), name='country-list'),
    path("countries/create", CountryCreateView.as_view(), name='country-create'),
    path("countries/<int:id>/update", CountryUpdateView.as_view(), name='country-update'),
    path("countries/<int:id>/delete", CountryDeleteView.as_view(), name='country-delete'),

    path("cities", CityListView.as_view(), name='city-list'),
    path("cities/create", CityCreateView.as_view(), name='city-create'),
    path("cities/<int:id>/update", CityUpdateView.as_view(), name='city-update'),
    path("cities/<int:id>/delete", CityDeleteView.as_view(), name='city-delete')
]
