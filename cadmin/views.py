from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.db import transaction
from django.db.models import Count, Q
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .forms import (
    UserForm,
    PsychologistApproachForm,
    PsychologistSpecializationForm,
    PsychologistStatusForm,
    PsychologistFormatForm,
    PsychologistThemeForm,
    PsychologistEducationForm,
    PsychologistSecondaryEducationForm,
    PsychologistLanguageForm,
    PsychologistProfileFormSet,
    CountryForm,
    CityForm,
)
from users.models import UserTypes
from psychologists.models import (
    PsychologistStatus,
    PsychologistApproach,
    PsychologistSpecialization,
    PsychologistWorkFormat,
    PsychologistTheme,
    PsychologistEducation,
    PsychologistSecondaryEducation,
    PsychologistLanguage,
)
from locations.models import City, Country

User = get_user_model()

import logging

logger = logging.getLogger(__name__)


class AdminOnlyView(LoginRequiredMixin, UserPassesTestMixin, View):
    permission_denied_message = 'Only admin has access to this view'

    def test_func(self):
        return self.request.user.user_type == UserTypes.admin_user.name


class MainAdminView(AdminOnlyView, TemplateView):
    template_name = 'cadmin/index.html'


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
    template_name = 'cadmin/locations/country_update.html'
    form_class = CountryForm
    context_object_name = 'country'

    def get_object(self):
        country_id = self.kwargs.get("id")
        return get_object_or_404(Country, id=country_id)

    def get_success_url(self):
        return reverse('country-update', kwargs={'id': self.kwargs['id']})


class CountryDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/locations/country_delete.html'
    context_object_name = 'country'

    def get_object(self):
        country_id = self.kwargs.get("id")
        return get_object_or_404(Country, id=country_id)

    def get_success_url(self):
        return reverse('country-list')


class CityListView(AdminOnlyView, ListView):
    model=City
    template_name = 'cadmin/locations/city_list.html'
    context_object_name = 'cities'

    def get_queryset(self):
        cities = City.objects.annotate(
            Count('psychologistuserprofile'),
            Count('regularuserprofile')).filter(
            Q(psychologistuserprofile__count__gt=0) | Q(regularuserprofile__count=0))
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
        city_id = self.kwargs.get("id")
        city = get_object_or_404(City, id=city_id)
        if city.regularuserprofile_set.count():
            raise PermissionDenied("You cant update city which refers not to psychologist profile")
        return city

    def get_success_url(self):
        return reverse('city-update', kwargs={'id': self.kwargs['id']})


class CityDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/locations/city_delete.html'
    context_object_name = 'city'

    def get_object(self):
        city_id = self.kwargs.get("id")
        city = get_object_or_404(City, id=city_id)
        if city.regularuserprofile_set.count() or city.psychologistuserprofile_set.count():
            raise PermissionDenied("You cant delete city which refers to profile")
        return city

    def get_success_url(self):
        return reverse('city-list')


class UserCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/users/user_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user-create')


class UserDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/users/user_delete.html'
    context_object_name = 'user'

    def get_object(self):
        user_id = self.kwargs.get("id")
        return get_object_or_404(User, id=user_id)

    def get_success_url(self):
        return reverse('psy-list')


class PsychologistUserListView(AdminOnlyView, ListView):
    template_name = 'cadmin/psychologists/psy_list.html'
    context_object_name = 'psychologists'

    def get_queryset(self):
        return User.objects.filter(user_type=UserTypes.psychologist_user.name)


class PsychologistUserAndProfileCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_user_profile_create.html'
    form_class = UserForm
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('psy-user-profile-create')

    def get_context_data(self, **kwargs):
        data = super(PsychologistUserAndProfileCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['profile'] = PsychologistProfileFormSet(self.request.POST, self.request.FILES)
        else:
            data['profile'] = PsychologistProfileFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        profile = context['profile']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if profile.is_valid():
                profile.instance = self.object
                profile.save()
        return super(PsychologistUserAndProfileCreateView, self).form_valid(form)


class PsychologistUserAndProfileUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_user_profile_update.html'
    form_class = UserForm
    context_object_name = 'user'

    def get_object(self):
        user_id = self.kwargs.get("id")
        return get_object_or_404(User, id=user_id)

    def get_success_url(self):
        return reverse('psy-user-profile-update', kwargs={'id': self.kwargs['id']})

    def get_context_data(self, **kwargs):
        data = super(PsychologistUserAndProfileUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['profile'] = PsychologistProfileFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['profile'] = PsychologistProfileFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        profile = context['profile']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if profile.is_valid():
                profile.instance = self.object
                profile.save()
        return super(PsychologistUserAndProfileUpdateView, self).form_valid(form)


class PsychologistStatusListView(AdminOnlyView, ListView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/psy_status_list.html'
    context_object_name = 'statuses'


class PsychologistStatusCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_status_create.html'
    form_class = PsychologistStatusForm

    def get_success_url(self):
        return reverse('psy-status-create')


class PsychologistStatusCreateAsModalView(PsychologistStatusCreateView):
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class PsychologistStatusUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_status_update.html'
    form_class = PsychologistStatusForm
    context_object_name = 'status'

    def get_object(self):
        status_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistStatus, id=status_id)

    def get_success_url(self):
        return reverse('psy-status-update', kwargs={'id': self.kwargs['id']})


class PsychologistStatusDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_status_delete.html'
    context_object_name = 'status'

    def get_object(self):
        status_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistStatus, id=status_id)

    def get_success_url(self):
        return reverse('psy-status-list')


class PsychologistApproachListView(AdminOnlyView, ListView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/psy_approach_list.html'
    context_object_name = 'approaches'


class PsychologistApproachCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_approach_create.html'
    form_class = PsychologistApproachForm

    def get_success_url(self):
        return reverse('psy-approach-create')


class PsychologistApproachUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_approach_update.html'
    form_class = PsychologistApproachForm
    context_object_name = 'approach'

    def get_object(self):
        approach_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistApproach, id=approach_id)

    def get_success_url(self):
        return reverse('psy-approach-update', kwargs={'id': self.kwargs['id']})


class PsychologistApproachDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_approach_delete.html'
    context_object_name = 'approach'

    def get_object(self):
        approach_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistApproach, id=approach_id)

    def get_success_url(self):
        return reverse('psy-approach-list')


class PsychologistSpecializationListView(AdminOnlyView, ListView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/psy_specialization_list.html'
    context_object_name = 'specializations'


class PsychologistSpecializationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_specialization_create.html'
    form_class = PsychologistSpecializationForm

    def get_success_url(self):
        return reverse('psy-specialization-create')


class PsychologistSpecializationUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_specialization_update.html'
    form_class = PsychologistSpecializationForm
    context_object_name = 'specialization'

    def get_object(self):
        specialization_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistSpecialization, id=specialization_id)

    def get_success_url(self):
        return reverse('psy-specialization-update', kwargs={'id': self.kwargs['id']})


class PsychologistSpecializationDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_specialization_delete.html'
    context_object_name = 'specialization'

    def get_object(self):
        specialization_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistSpecialization, id=specialization_id)

    def get_success_url(self):
        return reverse('psy-specialization-list')


class PsychologistFormatListView(AdminOnlyView, ListView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/psy_format_list.html'
    context_object_name = 'formats'


class PsychologistFormatCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_format_create.html'
    form_class = PsychologistFormatForm

    def get_success_url(self):
        return reverse('psy-format-create')


class PsychologistFormatUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_format_update.html'
    form_class = PsychologistFormatForm
    context_object_name = 'format'

    def get_object(self):
        format_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistWorkFormat, id=format_id)

    def get_success_url(self):
        return reverse('psy-format-update', kwargs={'id': self.kwargs['id']})


class PsychologistFormatDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_format_delete.html'
    context_object_name = 'format'

    def get_object(self):
        format_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistWorkFormat, id=format_id)

    def get_success_url(self):
        return reverse('psy-format-list')


class PsychologistThemeListView(AdminOnlyView, ListView):
    model = PsychologistTheme
    template_name = 'cadmin/psychologists/psy_theme_list.html'
    context_object_name = 'themes'


class PsychologistThemeCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_theme_create.html'
    form_class = PsychologistThemeForm

    def get_success_url(self):
        return reverse('psy-theme-create')


class PsychologistThemeUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_theme_update.html'
    form_class = PsychologistThemeForm
    context_object_name = 'theme'

    def get_object(self):
        theme_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistTheme, id=theme_id)

    def get_success_url(self):
        return reverse('psy-theme-update', kwargs={'id': self.kwargs['id']})


class PsychologistThemeDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_theme_delete.html'
    context_object_name = 'theme'

    def get_object(self):
        theme_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistTheme, id=theme_id)

    def get_success_url(self):
        return reverse('psy-theme-list')


class PsychologistEducationListView(AdminOnlyView, ListView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/psy_education_list.html'
    context_object_name = 'educations'


class PsychologistEducationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_education_create.html'
    form_class = PsychologistEducationForm

    def get_success_url(self):
        return reverse('psy-education-create')


class PsychologistEducationUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_education_update.html'
    form_class = PsychologistEducationForm
    context_object_name = 'education'

    def get_object(self):
        education_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistEducation, id=education_id)

    def get_success_url(self):
        return reverse('psy-education-update', kwargs={'id': self.kwargs['id']})


class PsychologistEducationDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_education_delete.html'
    context_object_name = 'education'

    def get_object(self):
        education_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistEducation, id=education_id)

    def get_success_url(self):
        return reverse('psy-education-list')


class PsychologistSecondaryEducationListView(AdminOnlyView, ListView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/psy_secondary_education_list.html'
    context_object_name = 'secondary_educations'


class PsychologistSecondaryEducationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_secondary_education_create.html'
    form_class = PsychologistSecondaryEducationForm

    def get_success_url(self):
        return reverse('psy-secondary-education-create')


class PsychologistSecondaryEducationUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_secondary_education_update.html'
    form_class = PsychologistSecondaryEducationForm
    context_object_name = 'secondary_education'

    def get_object(self):
        secondary_education_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistSecondaryEducation, id=secondary_education_id)

    def get_success_url(self):
        return reverse('psy-secondary-education-update', kwargs={'id': self.kwargs['id']})


class PsychologistSecondaryEducationDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_secondary_education_delete.html'
    context_object_name = 'secondary_education'

    def get_object(self):
        secondary_education_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistSecondaryEducation, id=secondary_education_id)

    def get_success_url(self):
        return reverse('psy-secondary-education-list')


class PsychologistLanguageListView(AdminOnlyView, ListView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/psy_language_list.html'
    context_object_name = 'languages'


class PsychologistLanguageCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_language_create.html'
    form_class = PsychologistLanguageForm

    def get_success_url(self):
        return reverse('psy-language-create')


class PsychologistLanguageUpdateView(AdminOnlyView, UpdateView):
    template_name = 'cadmin/psychologists/psy_language_update.html'
    form_class = PsychologistLanguageForm
    context_object_name = 'language'

    def get_object(self):
        language_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistLanguage, id=language_id)

    def get_success_url(self):
        return reverse('psy-language-update', kwargs={'id': self.kwargs['id']})


class PsychologistLanguageDeleteView(AdminOnlyView, DeleteView):
    template_name = 'cadmin/psychologists/psy_language_delete.html'
    context_object_name = 'language'

    def get_object(self):
        language_id = self.kwargs.get("id")
        return get_object_or_404(PsychologistLanguage, id=language_id)

    def get_success_url(self):
        return reverse('psy-language-list')
