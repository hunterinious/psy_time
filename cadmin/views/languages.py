from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistLanguageForm
from psychologists.models import PsychologistLanguage


class PsyLanguageListView(AdminOnlyView, ListView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/languages/psy_language_list.html'
    context_object_name = 'languages'


class PsyLanguageCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/languages/psy_language_create.html'
    form_class = PsychologistLanguageForm

    def get_success_url(self):
        return reverse('psy-language-create')


class PsyLanguageUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/languages/psy_language_update.html'
    form_class = PsychologistLanguageForm
    context_object_name = 'language'

    def get_success_url(self):
        return reverse('psy-language-update', kwargs={'pk': self.kwargs['pk']})


class PsyLanguageDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/languages/psy_language_delete.html'
    context_object_name = 'language'

    def get_success_url(self):
        return reverse('psy-language-list')
