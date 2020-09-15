from django.urls import path
from .views import PsyProfileListView


urlpatterns = [
    path('',  PsyProfileListView.as_view(), name="api-psy-list")
]