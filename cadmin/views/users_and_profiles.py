from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import transaction
from django.views.generic import (
    CreateView,
    UpdateView,
)
from .core import AdminOnlyView
from cadmin.forms import (
    UserCreateForm,
    UserUpdateForm,
    PsyProfileFormSet,
)


User = get_user_model()


class PsyUserAndProfileCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_user_profile_create.html'
    form_class = UserCreateForm
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('psy-user-profile-create')

    def get_context_data(self, **kwargs):
        data = super(PsyUserAndProfileCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['profile'] = PsyProfileFormSet(self.request.POST, self.request.FILES)
        else:
            data['profile'] = PsyProfileFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        profile = context['profile']
        with transaction.atomic():
            self.object = form.save()
            if profile.is_valid():
                profile.instance = self.object
                profile.save()
        return super(PsyUserAndProfileCreateView, self).form_valid(form)


class PsyUserAndProfileUpdateView(UpdateView):
    template_name = 'cadmin/psychologists/psy_user_profile_update.html'
    form_class = UserUpdateForm
    context_object_name = 'user'

    def get_object(self):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, id=user_id)

    def get_success_url(self):
        return reverse('psy-user-profile-update', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        data = super(PsyUserAndProfileUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['profile'] = PsyProfileFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['profile'] = PsyProfileFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        profile = context['profile']
        with transaction.atomic():
            self.object = form.save()
            if profile.is_valid():
                profile.instance = self.object
                profile.save()
        return super(PsyUserAndProfileUpdateView, self).form_valid(form)
