from django.shortcuts import get_object_or_404, render
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.db import transaction
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
    HelpForm,
)
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
from core.models import Help

from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views import View

User = get_user_model()


class AdminOnlyView(LoginRequiredMixin, UserPassesTestMixin, View):
    permission_denied_message = 'Only admin has access to this view'

    def test_func(self):
        return self.request.user.user_type == User.UserTypes.ADMIN_USER


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


class UserCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/users/user_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user-create')


class UserDeleteView(AdminOnlyView, DeleteView):
    model = User
    template_name = 'cadmin/users/user_delete.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('psy-list')


class PsychologistUserListView(AdminOnlyView, ListView):
    template_name = 'cadmin/psychologists/psy_list.html'
    context_object_name = 'psychologists'

    def get_queryset(self):
        return User.objects.get_psychologists_users()


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
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, id=user_id)

    def get_success_url(self):
        return reverse('psy-user-profile-update', kwargs={'pk': self.kwargs['pk']})

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


class DynamicPsyUserOperationsView(AdminOnlyView, View):
    form_class = PsychologistStatusForm
    template_name = None

    def save_status_form(self, request, form, method):
        data = dict()

        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['name'] = form.data['name']
        else:
            data['form_is_valid'] = False

        context = {'form': form, 'modal': True}
        data['method'] = method
        data['html_form'] = render_to_string(self.template_name,
                                             context,
                                             request=request
                                             )
        return data


class PsychologistStatusDynamicCreateView(DynamicPsyUserOperationsView):
    template_name = 'cadmin/psychologists/psy_status_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        data = self.save_status_form(request, form, 'get')
        return JsonResponse(data)

    def post(self, request):
        form = self.form_class(request.POST)
        data = self.save_status_form(request, form, 'create')
        return JsonResponse(data)


class PsychologistStatusDynamicUpdateView(DynamicPsyUserOperationsView):
    template_name = 'cadmin/psychologists/psy_status_update_dynamic.html'

    def get(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        form = self.form_class(instance=status)
        data = self.save_status_form(request, form, 'get')
        return JsonResponse(data)

    def post(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        form = self.form_class(request.POST, instance=status)
        data = self.save_status_form(request, form, 'update')
        return JsonResponse(data)


class PsychologistStatusUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/psy_status_update.html'
    form_class = PsychologistStatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('psy-status-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistStatusDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/psy_status_delete.html'
    context_object_name = 'status'

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
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/psy_approach_update.html'
    form_class = PsychologistApproachForm
    context_object_name = 'approach'

    def get_success_url(self):
        return reverse('psy-approach-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistApproachDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/psy_approach_delete.html'
    context_object_name = 'approach'

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
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/psy_specialization_update.html'
    form_class = PsychologistSpecializationForm
    context_object_name = 'specialization'

    def get_success_url(self):
        return reverse('psy-specialization-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistSpecializationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/psy_specialization_delete.html'
    context_object_name = 'specialization'

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
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/psy_format_update.html'
    form_class = PsychologistFormatForm
    context_object_name = 'format'

    def get_success_url(self):
        return reverse('psy-format-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistFormatDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/psy_format_delete.html'
    context_object_name = 'format'

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
    model = PsychologistTheme
    template_name = 'cadmin/psychologists/psy_theme_update.html'
    form_class = PsychologistThemeForm
    context_object_name = 'theme'

    def get_success_url(self):
        return reverse('psy-theme-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistThemeDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistTheme
    template_name = 'cadmin/psychologists/psy_theme_delete.html'
    context_object_name = 'theme'

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
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/psy_education_update.html'
    form_class = PsychologistEducationForm
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('psy-education-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistEducationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/psy_education_delete.html'
    context_object_name = 'education'

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
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/psy_secondary_education_update.html'
    form_class = PsychologistSecondaryEducationForm
    context_object_name = 'secondary_education'

    def get_success_url(self):
        return reverse('psy-secondary-education-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistSecondaryEducationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/psy_secondary_education_delete.html'
    context_object_name = 'secondary_education'

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
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/psy_language_update.html'
    form_class = PsychologistLanguageForm
    context_object_name = 'language'

    def get_success_url(self):
        return reverse('psy-language-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistLanguageDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/psy_language_delete.html'
    context_object_name = 'language'

    def get_success_url(self):
        return reverse('psy-language-list')


class HelpRequestListView(AdminOnlyView, ListView):
    model = Help
    template_name = 'cadmin/help_requests/help_request_list.html'
    context_object_name = 'help_requests'


class HelpRequestUpdateView(AdminOnlyView, UpdateView):
    model = Help
    template_name = 'cadmin/help_requests/help_request_update.html'
    form_class = HelpForm
    context_object_name = 'help_request'

    def get_success_url(self):
        return reverse('help-request-update', kwargs={'pk': self.kwargs['pk']})
