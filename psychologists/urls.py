from django.urls import path
from .views import (
    PsyProfileListView,
    PsyPublicProfileView,
    PsyExtendedPublicProfileView,
    PsyProfileCriteriaView,
    PsyProfileFilteredListView,
    RandomPsyProfileView,
    HowToChoosePsychologistView
)


urlpatterns = [
    path('',  PsyProfileListView.as_view(), name="api-psy-list"),
    path('public-profile/<int:pk>/detail',  PsyPublicProfileView.as_view(),
         name="api-psy-public-profile-detail"),
    path('public-extended-profile/<int:pk>/detail', PsyExtendedPublicProfileView.as_view(),
         name="api-psy-public-extended-profile-detail"),
    path('criteria', PsyProfileCriteriaView.as_view(), name="api-psy-criteria"),
    path('filter', PsyProfileFilteredListView.as_view(), name="api-psy-filtered"),
    path('random', RandomPsyProfileView.as_view(), name="api-random-psy"),
    path('how-to-choose-psychologist', HowToChoosePsychologistView.as_view(), name="api-how-to-choose-psy"),
]
