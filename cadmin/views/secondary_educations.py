from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistSecondaryEducationForm
from psychologists.models import PsychologistSecondaryEducation


class PsychologistSecondaryEducationListView(AdminOnlyView, ListView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_list.html'
    context_object_name = 'secondary_educations'


class PsychologistSecondaryEducationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_create.html'
    form_class = PsychologistSecondaryEducationForm

    def get_success_url(self):
        return reverse('psy-secondary-education-create')


class PsychologistSecondaryEducationUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_update.html'
    form_class = PsychologistSecondaryEducationForm
    context_object_name = 'secondary_education'

    def get_success_url(self):
        return reverse('psy-secondary-education-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistSecondaryEducationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_delete.html'
    context_object_name = 'secondary_education'

    def get_success_url(self):
        return reverse('psy-secondary-education-list')
