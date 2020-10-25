from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistApproachForm
from psychologists.models import PsychologistApproach


class PsychologistApproachListView(AdminOnlyView, ListView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/approaches/psy_approach_list.html'
    context_object_name = 'approaches'


class PsychologistApproachCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/approaches/psy_approach_create.html'
    form_class = PsychologistApproachForm

    def get_success_url(self):
        return reverse('psy-approach-create')


class PsychologistApproachUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/approaches/psy_approach_update.html'
    form_class = PsychologistApproachForm
    context_object_name = 'approach'

    def get_success_url(self):
        return reverse('psy-approach-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistApproachDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/approaches/psy_approach_delete.html'
    context_object_name = 'approach'

    def get_success_url(self):
        return reverse('psy-approach-list')
