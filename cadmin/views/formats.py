from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistFormatForm
from psychologists.models import PsychologistWorkFormat


class PsyFormatListView(AdminOnlyView, ListView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/formats/psy_format_list.html'
    context_object_name = 'formats'


class PsyFormatCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/formats/psy_format_create.html'
    form_class = PsychologistFormatForm

    def get_success_url(self):
        return reverse('psy-format-create')


class PsyFormatUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/formats/psy_format_update.html'
    form_class = PsychologistFormatForm
    context_object_name = 'format'

    def get_success_url(self):
        return reverse('psy-format-update', kwargs={'pk': self.kwargs['pk']})


class PsyFormatDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/formats/psy_format_delete.html'
    context_object_name = 'format'

    def get_success_url(self):
        return reverse('psy-format-list')
