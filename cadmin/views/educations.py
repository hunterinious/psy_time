from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistEducationForm
from psychologists.models import PsychologistEducation


class PsychologistEducationListView(AdminOnlyView, ListView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/educations/psy_education_list.html'
    context_object_name = 'educations'


class PsychologistEducationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/educations/psy_education_create.html'
    form_class = PsychologistEducationForm

    def get_success_url(self):
        return reverse('psy-education-create')


class PsychologistEducationUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/educations/psy_education_update.html'
    form_class = PsychologistEducationForm
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('psy-education-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistEducationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/educations/psy_education_delete.html'
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('psy-education-list')
