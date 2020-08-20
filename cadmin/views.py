from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    FormView
)
from .forms import (
    LoginForm,
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

User = get_user_model()


class LoginView(FormView):
    template_name = 'cadmin/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('psy-list')

    def form_valid(self, form):
        data = form.cleaned_data

        user = authenticate(email=data['email'], password=data['password'])
        if user is not None and user.user_type == UserTypes.admin_user.name:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                            please try again')
            return HttpResponseRedirect(reverse_lazy('login'))


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


class PsychologistUserListView(ListView):
    template_name = 'cadmin/psy_list.html'
    context_object_name = 'psychologists'

    def get_queryset(self):
        return User.objects.filter(user_type=UserTypes.psychologist_user.name)


class PsychologistUserAndProfileCreateView(CreateView):
    template_name = 'cadmin/psy_user_profile_create.html'
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


class PsychologistUserAndProfileUpdateView(UpdateView):
    template_name = 'cadmin/psy_user_profile_update.html'
    form_class = UserForm
    context_object_name = 'user'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)

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


