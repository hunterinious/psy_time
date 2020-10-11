from django.urls import path
from .views import (
    WorldCountriesListView,
    HelpView
)


urlpatterns = [
    path('countries',  WorldCountriesListView.as_view(), name="api-world-countries-list"),
    path('help', HelpView.as_view(), name="api-help")
]
