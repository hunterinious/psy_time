from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PsyProfileListView,
    PsyProfileCriteriaView,
    PsyProfileFilteredListView,
    HowToChoosePsychologistView
)


urlpatterns = [
    path('',  PsyProfileListView.as_view(), name="api-psy-list"),
    path('criteria', PsyProfileCriteriaView.as_view(), name="api-psy-criteria"),
    re_path('^filter/(?P<ages>.+)'
            '(?P<genders>.+)'
            '(?P<statuses>.+)'
            '(?P<formats>.+)'
            '(?P<themes>.+)'
            '(?P<approaches>.+)'
            '(?P<specializations>.+)'
            '(?P<educations>.+)'
            '(?P<secondary>.+)'
            '(?P<languages>)$'
            , PsyProfileFilteredListView.as_view(), name="api-psy-filtered"),
    path('how-to-choose-psychologist', HowToChoosePsychologistView.as_view(), name="api-how-to-choose-psy"),
]
