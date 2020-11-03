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
from cadmin.forms import CityForm, CountryForm, CountryDynamicForm, CityFormSet
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


class CountryAndCityCreateView(AdminOnlyView, View):
    template_name = 'cadmin/locations/country_city_create_dynamic.html'
    form_class = CountryDynamicForm
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

        if form.is_valid():
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


class CountryAndCityUpdateView(AdminOnlyView, View):
    template_name = 'cadmin/locations/country_city_update_dynamic.html'
    serializer_class = CityDynamicSerializer
    form_class = CountryDynamicForm

    def get(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        self.object = city.country
        form = self.form_class(instance=self.object)
        return self.save_form(request, form)

    def post(self, request, pk):
        self.object = get_object_or_404(Country, pk=pk)
        form = self.form_class(request.POST, instance=self.object)
        return self.save_form(request, form)

    def save_form(self, request, form):
        data = dict()
        context = self.get_context_data()

        if form.is_valid():
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
            data['city'] = CityFormSet(self.request.POST, instance=self.object)
        else:
            data['city'] = CityFormSet(instance=self.object)
        return data

    def form_valid(self, form, city):
        with transaction.atomic():
            self.object = form.save()
            if city.is_valid():
                city.instance = self.object
                city.save()


class CountryAndCityDeleteView(AdminOnlyView, View):
    template_name = 'cadmin/locations/country_city_create_dynamic.html'
    serializer_class = CityDynamicSerializer
    form_class = CountryForm
    context_object_name = 'country'

    def get(self, request, *args, **kwargs):
        country = get_object_or_404(Country)
        form = self.form_class(instance=country)
        return self.save_form(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        country = Country.objects.safe_get_by_name(name=request.POST.get('name'))
        if country:
            form = self.form_class(request.POST, instance=country)
        else:
            form = self.form_class(request.POST)
        return self.save_form(request, form, *args, **kwargs)

    def save_form(self, request, form, *args, **kwargs):
        data = dict()
        context = self.get_context_data(**kwargs)

        if form.is_valid():
            self.form_valid(form)
            data['form_is_valid'] = True
            data['data'] = self.serializer_class(City.objects.get_all(), many=True).data
        else:
            data['form_is_valid'] = False

        context['form'] = form
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        data = super(CountryAndCityUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['city'] = CityFormSet(self.request.POST)
        else:
            data['city'] = CityFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        city = context['city']
        with transaction.atomic():
            self.object = form.save()
            if city.is_valid():
                city.instance = self.object
                city.save()
