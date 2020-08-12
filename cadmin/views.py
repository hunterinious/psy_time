from django.urls import reverse
from django.views.generic import CreateView
from .forms import (
    UserForm,
    PsychologistProfileForm,
    PsychologistStatusForm,
    PsychologistSecondaryEducationForm,
    CountryForm,
    CityForm,
)


class CountryCreateView(CreateView):
    template_name = 'cadmin/country_create.html'
    form_class = CountryForm

    def get_success_url(self):
        return reverse('country-create')


class CityCreateView(CreateView):
    template_name = 'cadmin/city_create.html'
    form_class = CityForm

    def get_success_url(self):
        return reverse('city-create')


class UserCreateView(CreateView):
    template_name = 'cadmin/user_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user-create')


class PsychologistProfileCreateView(CreateView):
    template_name = 'cadmin/psy_profile_create.html'
    form_class = PsychologistProfileForm

    def get_success_url(self):
        return reverse('psy-profile-create')


class PsychologistStatusCreateView(CreateView):
    template_name = 'cadmin/psy_status_create.html'
    form_class = PsychologistStatusForm

    def get_success_url(self):
        return reverse('psy-status-create')


class PsychologistSecondaryEducationCreateView(CreateView):
    template_name = 'cadmin/psy_secondary_education_create.html'
    form_class = PsychologistSecondaryEducationForm

    def get_success_url(self):
        return reverse('psy-secondary-education-create')
