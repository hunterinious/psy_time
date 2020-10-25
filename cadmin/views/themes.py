from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistThemeForm
from psychologists.models import PsychologistTheme


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
