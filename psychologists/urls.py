from django.urls import path
from .views import PsyProfileListView, PsyProfileFilterCriteriaView


urlpatterns = [
    path('',  PsyProfileListView.as_view(), name="api-psy-list"),
    path('criteria', PsyProfileFilterCriteriaView.as_view(), name="api-psy-criteria")
]