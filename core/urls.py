from django.urls import path
from .views import (
    WorldCountriesListView,
    HelpCreateView
)


urlpatterns = [
    path('countries',  WorldCountriesListView.as_view(), name="api-world-countries-list"),
    path('help', HelpCreateView.as_view(), name="api-help-create")
]
