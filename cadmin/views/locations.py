from django.shortcuts import get_object_or_404
from django.db import transaction
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    View
)
from .core import AdminOnlyView
from cadmin.forms import CityForm, CountryForm, CityFormSet
from locations.models import City, Country
from locations.serializers import CityDynamicSerializer


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
        if City.objects.is_related_to_regular_user_profile(city):
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
        if City.objects.is_related_to_profiles(city):
            raise PermissionDenied("You cant delete city which refers to profile")
        return city

    def get_success_url(self):
        return reverse('city-list')


class CountryAndCityDynamicCreateView(AdminOnlyView, View):
    template_name = 'cadmin/locations/country_city_create_dynamic.html'
    form_class = CountryForm
    serializer_class = CityDynamicSerializer

    def get(self, request):
        form = self.form_class()
        return self.save_form(request, form)

    def post(self, request):
        country = Country.objects.safe_get_by_name(name=request.POST.get('name'))
        if country:
            form = self.form_class(request.POST, instance=country)
        else:
            form = self.form_class(request.POST)
        return self.save_form(request, form)

    def save_form(self, request, form):
        data = dict()
        context = self.get_context_data()

        if request.POST and form.is_valid():
            self.form_valid(form, context['city'])
            data['form_is_valid'] = True
            data['data'] = self.serializer_class(City.objects.get_all(), many=True).data
        else:
            data['form_is_valid'] = False

        context['form'] = form
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)

    def get_context_data(self):
        data = dict()
        if self.request.POST:
            data['city'] = CityFormSet(self.request.POST)
        else:
            data['city'] = CityFormSet()
        return data

    def form_valid(self, form, city):
        with transaction.atomic():
            self.object = form.save()
            if city.is_valid():
                city.instance = self.object
                city.save()


class CountryAndCityDynamicUpdateView(AdminOnlyView, View):
    template_name = 'cadmin/locations/country_city_update_dynamic.html'
    serializer_class = CityDynamicSerializer

    def get(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        country = city.country
        country_form = CountryForm(instance=country, prefix='country')
        city_form = CityForm(instance=city, prefix='city')
        return self.save_form(request, country_form, city_form)

    def post(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        country = city.country
        country_form = CountryForm(request.POST, instance=country, prefix='country')
        city_form = CityForm(request.POST, instance=city, prefix='city')
        return self.save_form(request, country_form, city_form)

    def save_form(self, request, country_form, city_form):
        data = dict()

        if request.POST and country_form.is_valid() and city_form.is_valid():
            self.forms_valid(country_form, city_form)
            data['form_is_valid'] = True
            data['data'] = self.serializer_class(City.objects.get_all(), many=True).data
        else:
            data['form_is_valid'] = False

        context = {'country_form': country_form, 'city_form': city_form}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)

    def forms_valid(self, country_form, city_form):
        with transaction.atomic():
            country = country_form.save()
            city = city_form.save(False)
            city.country = country
            city.save()


class CityDynamicDeleteView(AdminOnlyView, View):
    template_name = 'cadmin/locations/city_delete_dynamic.html'
    forbidden_template_name = 'cadmin/modal_403_refers_to_profiles.html'
    serializer_class = CityDynamicSerializer

    def get(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        return self.manage_delete(request, city)

    def post(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        return self.manage_delete(request, city)

    def manage_delete(self, request, city):
        data = dict()

        template = self.template_name

        if request.POST:
            deleted = City.objects.delete_by_name(name=city.name)

            if deleted:
                data['form_is_valid'] = True
                data['data'] = self.serializer_class(City.objects.get_all(), many=True).data
            else:
                template = self.forbidden_template_name

        context = {'instance': city}
        data['html_form'] = render_to_string(template, context, request=request)
        return JsonResponse(data)
