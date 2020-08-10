from django.urls import path
from .views import CountryCreateView, CityCreateView


urlpatterns = [
    path("countries/create", CountryCreateView.as_view(), name='country-create'),
    path("cities/create", CityCreateView.as_view(), name='city-create'),
]