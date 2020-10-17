from django.urls import path
from .views import (
    WorldCountryListView,
    HelpCreateView
)


urlpatterns = [
    path('countries',  WorldCountryListView.as_view(), name="api-world-countries-list"),
    path('help', HelpCreateView.as_view(), name="api-help-create")
]
