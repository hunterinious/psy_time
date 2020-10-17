from django.urls import path
from .views import (
    PsyProfileListView,
    PsyPublicProfileView,
    PsyExtendedPublicProfileView,
    PsyReviewListView,
    PsyProfileCriteriaView,
    PsyProfileFilteredListView,
    RandomPsyProfileView,
    HowToChoosePsyView
)


urlpatterns = [
    path('',  PsyProfileListView.as_view(), name="api-psy-list"),
    path('public-profile/<int:pk>/detail',  PsyPublicProfileView.as_view(),
         name="api-psy-public-profile-detail"),
    path('public-extended-profile/<int:pk>/detail', PsyExtendedPublicProfileView.as_view(),
         name="api-psy-public-extended-profile-detail"),
    path('reviews/<int:pk>/detail', PsyReviewListView.as_view(), name="api-psy-reviews"),
    path('criteria', PsyProfileCriteriaView.as_view(), name="api-psy-criteria"),
    path('filter', PsyProfileFilteredListView.as_view(), name="api-psy-filtered"),
    path('random', RandomPsyProfileView.as_view(), name="api-random-psy"),
    path('how-to-choose-psychologist', HowToChoosePsyView.as_view(), name="api-how-to-choose-psy")
]
