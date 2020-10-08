from django.urls import path
from .views import (
    PsyProfileListView,
    PsyProfileCriteriaView,
    PsyProfileFilteredListView,
    HowToChoosePsychologistView
)


urlpatterns = [
    path('',  PsyProfileListView.as_view(), name="api-psy-list"),
    path('criteria', PsyProfileCriteriaView.as_view(), name="api-psy-criteria"),
    path('filter', PsyProfileFilteredListView.as_view(), name="api-psy-filtered"),
    path('how-to-choose-psychologist', HowToChoosePsychologistView.as_view(), name="api-how-to-choose-psy"),
]
