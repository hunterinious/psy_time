from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    core,
    locations,
    users,
    users_and_profiles,
    statuses,
    formats,
    themes,
    approaches,
    specializations,
    educations,
    secondary_educations,
    languages,
    help_requests,
)

urlpatterns = [
    path("", core.MainAdminView.as_view(), name="admin-main"),

    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),

    path("users/create", users.UserCreateView.as_view(), name='user-create'),
    path("users/<int:pk>/delete", users.UserDeleteView.as_view(), name='user-delete'),

    path("psychologists-profiles/create", users_and_profiles.PsyUserAndProfileCreateView.as_view(),
         name='psy-user-profile-create'),
    path("psychologists-profiles/<int:pk>/update", users_and_profiles.PsyUserAndProfileUpdateView.as_view(),
         name='psy-user-profile-update'),
    path("psychologists", users.PsyUserListView.as_view(),
         name='psy-list'),

    path("psychologists/statuses", statuses.PsyStatusListView.as_view(),
         name='psy-status-list'),
    path("psychologists/statuses/create", statuses.PsyStatusCreateView.as_view(),
         name='psy-status-create'),
    path("psychologists/statuses/create-dynamic", statuses.PsyStatusDynamicCreateView.as_view(),
         name='psy-status-create-dynamic'),
    path("psychologists/statuses/<int:pk>/update", statuses.PsyStatusUpdateView.as_view(),
         name='psy-status-update'),
    path("psychologists/statuses/<int:pk>/update-dynamic", statuses.PsyStatusDynamicUpdateView.as_view(),
         name='psy-status-update-dynamic'),
    path("psychologists/statuses/<int:pk>/delete", statuses.PsyStatusDeleteView.as_view(),
         name='psy-status-delete'),
    path("psychologists/statuses/<int:pk>/delete-dynamic", statuses.PsyStatusDynamicDeleteView.as_view(),
         name='psy-status-delete-dynamic'),

    path("psychologists/approaches", approaches.PsyApproachListView.as_view(),
         name='psy-approach-list'),
    path("psychologists/approaches/create", approaches.PsyApproachCreateView.as_view(),
         name='psy-approach-create'),
    path("psychologists/approaches/create-dynamic", approaches.PsyApproachDynamicCreateView.as_view(),
         name='psy-approach-create-dynamic'),
    path("psychologists/approaches/<int:pk>/update", approaches.PsyApproachUpdateView.as_view(),
         name='psy-approach-update'),
    path("psychologists/approaches/<int:pk>/update-dynamic", approaches.PsyApproachDynamicUpdateView.as_view(),
         name='psy-approach-update-dynamic'),
    path("psychologists/approaches/<int:pk>/delete", approaches.PsyApproachDeleteView.as_view(),
         name='psy-approach-delete'),
    path("psychologists/approaches/<int:pk>/delete-dynamic", approaches.PsyApproachDynamicDeleteView.as_view(),
         name='psy-approach-delete-dynamic'),

    path("psychologists/specializations",
         specializations.PsySpecializationListView.as_view(),
         name='psy-specialization-list'),
    path("psychologists/specializations/create",
         specializations.PsySpecializationCreateView.as_view(),
         name='psy-specialization-create'),
    path("psychologists/specializations/create-dynamic",
         specializations.PsySpecializationDynamicCreateView.as_view(),
         name='psy-specialization-create-dynamic'),
    path("psychologists/specializations/<int:pk>/update",
         specializations.PsySpecializationUpdateView.as_view(),
         name='psy-specialization-update'),
    path("psychologists/specializations/<int:pk>/update-dynamic",
         specializations.PsySpecializationDynamicUpdateView.as_view(),
         name='psy-specialization-update-dynamic'),
    path("psychologists/specializations/<int:pk>/delete",
         specializations.PsySpecializationDeleteView.as_view(),
         name='psy-specialization-delete'),
    path("psychologists/specializations/<int:pk>/delete-dynamic",
         specializations.PsySpecializationDynamicDeleteView.as_view(),
         name='psy-specialization-delete-dynamic'),


    path("psychologists/formats", formats.PsyFormatListView.as_view(),
         name='psy-format-list'),
    path("psychologists/formats/create", formats.PsyFormatCreateView.as_view(),
         name='psy-format-create'),
    path("psychologists/formats/create-dynamic", formats.PsyFormatDynamicCreateView.as_view(),
         name='psy-format-create-dynamic'),
    path("psychologists/formats/<int:pk>/update", formats.PsyFormatUpdateView.as_view(),
         name='psy-format-update'),
    path("psychologists/formats/<int:pk>/update-dynamic", formats.PsyFormatDynamicUpdateView.as_view(),
         name='psy-format-update-dynamic'),
    path("psychologists/formats/<int:pk>/delete", formats.PsyFormatDeleteView.as_view(),
         name='psy-format-delete'),
    path("psychologists/formats/<int:pk>/delete-dynamic", formats.PsyFormatDynamicDeleteView.as_view(),
         name='psy-format-delete-dynamic'),

    path("psychologists/themes", themes.PsyThemeListView.as_view(),
         name='psy-theme-list'),
    path("psychologists/themes/create", themes.PsyThemeCreateView.as_view(),
         name='psy-theme-create'),
    path("psychologists/themes/create-dynamic", themes.PsyThemeDynamicCreateView.as_view(),
         name='psy-theme-create-dynamic'),
    path("psychologists/themes/<int:pk>/update", themes.PsyThemeUpdateView.as_view(),
         name='psy-theme-update'),
    path("psychologists/themes/<int:pk>/update-dynamic", themes.PsyThemeDynamicUpdateView.as_view(),
         name='psy-theme-update-dynamic'),
    path("psychologists/themes/<int:pk>/delete", themes.PsyThemeDeleteView.as_view(),
         name='psy-theme-delete'),
    path("psychologists/themes/<int:pk>/delete-dynamic", themes.PsyThemeDynamicDeleteView.as_view(),
         name='psy-theme-delete-dynamic'),

    path("psychologists/educations", educations.PsyEducationListView.as_view(),
         name='psy-education-list'),
    path("psychologists/educations/create", educations.PsyEducationCreateView.as_view(),
         name='psy-education-create'),
    path("psychologists/educations/create-dynamic", educations.PsyEducationDynamicCreateView.as_view(),
         name='psy-education-create-dynamic'),
    path("psychologists/educations/<int:pk>/update", educations.PsyEducationUpdateView.as_view(),
         name='psy-education-update'),
    path("psychologists/educations/<int:pk>/update-dynamic", educations.PsyEducationDynamicUpdateView.as_view(),
         name='psy-education-update-dynamic'),
    path("psychologists/educations/<int:pk>/delete", educations.PsyEducationDeleteView.as_view(),
         name='psy-education-delete'),
    path("psychologists/educations/<int:pk>/delete-dynamic", educations.PsyEducationDynamicDeleteView.as_view(),
         name='psy-education-delete-dynamic'),


    path("psychologists/secondary-educations",
         secondary_educations.PsySecondaryEducationListView.as_view(),
         name='psy-secondary-education-list'),
    path("psychologists/secondary-educations/create",
         secondary_educations.PsySecondaryEducationCreateView.as_view(),
         name='psy-secondary-education-create'),
    path("psychologists/secondary-educations/create-dynamic",
         secondary_educations.PsySecondaryEducationDynamicCreateView.as_view(),
         name='psy-secondary-education-create-dynamic'),
    path("psychologists/secondary-educations/<int:pk>/update",
         secondary_educations.PsySecondaryEducationUpdateView.as_view(),
         name='psy-secondary-education-update'),
    path("psychologists/secondary-educations/<int:pk>/update-dynamic",
         secondary_educations.PsySecondaryEducationDynamicUpdateView.as_view(),
         name='psy-secondary-education-update-dynamic'),
    path("psychologists/secondary-educations/<int:pk>/delete",
         secondary_educations.PsySecondaryEducationDeleteView.as_view(),
         name='psy-secondary-education-delete'),
    path("psychologists/secondary-educations/<int:pk>/delete-dynamic",
         secondary_educations.PsySecondaryEducationDynamicDeleteView.as_view(),
         name='psy-secondary-education-delete-dynamic'),

    path("psychologists/languages", languages.PsyLanguageListView.as_view(),
         name='psy-language-list'),
    path("psychologists/languages/create", languages.PsyLanguageCreateView.as_view(),
         name='psy-language-create'),
    path("psychologists/languages/create-dynamic", languages.PsyLanguageDynamicCreateView.as_view(),
         name='psy-language-create-dynamic'),
    path("psychologists/languages/<int:pk>/update", languages.PsyLanguageUpdateView.as_view(),
         name='psy-language-update'),
    path("psychologists/languages/<int:pk>/update-dynamic", languages.PsyLanguageDynamicUpdateView.as_view(),
         name='psy-language-update-dynamic'),
    path("psychologists/languages/<int:pk>/delete", languages.PsyLanguageDeleteView.as_view(),
         name='psy-language-delete'),
    path("psychologists/languages/<int:pk>/delete-dynamic", languages.PsyLanguageDynamicDeleteView.as_view(),
         name='psy-language-delete-dynamic'),

    path("countries", locations.CountryListView.as_view(), name='country-list'),
    path("countries/create", locations.CountryCreateView.as_view(), name='country-create'),
    path("countries/<int:pk>/update", locations.CountryUpdateView.as_view(), name='country-update'),
    path("countries/<int:pk>/delete", locations.CountryDeleteView.as_view(), name='country-delete'),

    path("cities", locations.CityListView.as_view(), name='city-list'),
    path("cities/create", locations.CityCreateView.as_view(), name='city-create'),
    path("cities/<int:pk>/update", locations.CityUpdateView.as_view(), name='city-update'),
    path("cities/<int:pk>/delete", locations.CityDeleteView.as_view(), name='city-delete'),

    path("help-requests", help_requests.HelpRequestListView.as_view(), name='help-request-list'),
    path("help-requests/<int:pk>/update", help_requests.HelpRequestUpdateView.as_view(), name='help-request-update'),
]
