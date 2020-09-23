from django.urls import path
from .views import (
    PsyProfileListView,
    PsyProfileFilterCriteriaView,
    HowToChoosePsychologistView
)


urlpatterns = [
    path('',  PsyProfileListView.as_view(), name="api-psy-list"),
    path('criteria', PsyProfileFilterCriteriaView.as_view(), name="api-psy-criteria"),
    path('how_to_choose_psychologist', HowToChoosePsychologistView.as_view(), name="api-how-to-choose-psy"),
]