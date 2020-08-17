from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    UpdateView,
)

from .forms import (
    UserForm,
    PsychologistProfileForm,
    PsychologistApproachForm,
    PsychologistSpecializationForm,
    PsychologistStatusForm,
    PsychologistFormatForm,
    PsychologistThemeForm,
    PsychologistEducationForm,
    PsychologistSecondaryEducationForm,
    PsychologistLanguageForm,
    CountryForm,
    CityForm,
)
from psychologists.models import PsychologistUserProfile


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


class PsychologistProfileUpdateView(UpdateView):
    template_name = 'cadmin/psy_profile_update.html'
    form_class = PsychologistProfileForm
    context_object_name = 'profile'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(PsychologistUserProfile, id=id_)

    def get_success_url(self):
        return reverse('psy-profile-update', kwargs={'id': self.kwargs['id']})


class PsychologistStatusCreateView(CreateView):
    template_name = 'cadmin/psy_status_create.html'
    form_class = PsychologistStatusForm

    def get_success_url(self):
        return reverse('psy-status-create')


class PsychologistApproachCreateView(CreateView):
    template_name = 'cadmin/psy_approach_create.html'
    form_class = PsychologistApproachForm

    def get_success_url(self):
        return reverse('psy-approach-create')


class PsychologistSpecializationCreateView(CreateView):
    template_name = 'cadmin/psy_specialization_create.html'
    form_class = PsychologistSpecializationForm

    def get_success_url(self):
        return reverse('psy-specialization-create')


class PsychologistFormatCreateView(CreateView):
    template_name = 'cadmin/psy_format_create.html'
    form_class = PsychologistFormatForm

    def get_success_url(self):
        return reverse('psy-format-create')


class PsychologistThemeCreateView(CreateView):
    template_name = 'cadmin/psy_theme_create.html'
    form_class = PsychologistThemeForm

    def get_success_url(self):
        return reverse('psy-theme-create')


class PsychologistEducationCreateView(CreateView):
    template_name = 'cadmin/psy_education_create.html'
    form_class = PsychologistEducationForm

    def get_success_url(self):
        return reverse('psy-education-create')


class PsychologistSecondaryEducationCreateView(CreateView):
    template_name = 'cadmin/psy_secondary_education_create.html'
    form_class = PsychologistSecondaryEducationForm

    def get_success_url(self):
        return reverse('psy-secondary-education-create')


class PsychologistLanguageCreateView(CreateView):
    template_name = 'cadmin/psy_language_create.html'
    form_class = PsychologistLanguageForm

    def get_success_url(self):
        return reverse('psy-language-create')


