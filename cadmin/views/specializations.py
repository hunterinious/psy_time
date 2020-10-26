from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistSpecializationForm
from psychologists.models import PsychologistSpecialization


class PsySpecializationListView(AdminOnlyView, ListView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/specializations/psy_specialization_list.html'
    context_object_name = 'specializations'


class PsySpecializationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/specializations/psy_specialization_create.html'
    form_class = PsychologistSpecializationForm

    def get_success_url(self):
        return reverse('psy-specialization-create')


class PsySpecializationUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/specializations/psy_specialization_update.html'
    form_class = PsychologistSpecializationForm
    context_object_name = 'specialization'

    def get_success_url(self):
        return reverse('psy-specialization-update', kwargs={'pk': self.kwargs['pk']})


class PsySpecializationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/specializations/psy_specialization_delete.html'
    context_object_name = 'specialization'

    def get_success_url(self):
        return reverse('psy-specialization-list')
