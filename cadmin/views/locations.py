from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import CityForm, CountryForm
from locations.models import City, Country


class CountryListView(AdminOnlyView, ListView):
    model = Country
    template_name = 'cadmin/locations/country_list.html'
    context_object_name = 'countries'


class CountryCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/locations/country_create.html'
    form_class = CountryForm

    def get_success_url(self):
        return reverse('country-create')


class CountryUpdateView(AdminOnlyView, UpdateView):
    model = Country
    template_name = 'cadmin/locations/country_update.html'
    form_class = CountryForm
    context_object_name = 'country'

    def get_success_url(self):
        return reverse('country-update', kwargs={'pk': self.kwargs['pk']})


class CountryDeleteView(AdminOnlyView, DeleteView):
    model = Country
    template_name = 'cadmin/locations/country_delete.html'
    context_object_name = 'country'

    def get_success_url(self):
        return reverse('country-list')


class CityListView(AdminOnlyView, ListView):
    model = City
    template_name = 'cadmin/locations/city_list.html'
    context_object_name = 'cities'

    def get_queryset(self):
        cities = City.objects.get_cities_not_related_to_profiles()
        return cities


class CityCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/locations/city_create.html'
    form_class = CityForm

    def get_success_url(self):
        return reverse('city-create')


class CityUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/locations/city_update.html'
    form_class = CityForm
    context_object_name = 'city'

    def get_object(self):
        city_id = self.kwargs.get("pk")
        city = get_object_or_404(City, id=city_id)
        if city.is_related_to_regular_user_profile():
            raise PermissionDenied("You cant update city which refers not to psychologist profile")
        return city

    def get_success_url(self):
        return reverse('city-update', kwargs={'pk': self.kwargs['pk']})


class CityDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/locations/city_delete.html'
    context_object_name = 'city'

    def get_object(self):
        city_id = self.kwargs.get("pk")
        city = get_object_or_404(City, id=city_id)
        if city.is_related_to_profiles():
            raise PermissionDenied("You cant delete city which refers to profile")
        return city

    def get_success_url(self):
        return reverse('city-list')
