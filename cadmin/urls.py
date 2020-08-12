from django.urls import path
from .views import UserCreateView, CountryCreateView, CityCreateView


urlpatterns = [
    path("users/create", UserCreateView.as_view(), name='user-create'),
    path("countries/create", CountryCreateView.as_view(), name='country-create'),
    path("cities/create", CityCreateView.as_view(), name='city-create'),
]
