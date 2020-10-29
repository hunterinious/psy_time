from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView, PsyDynamicOperationsView
from cadmin.forms import PsyLanguageForm
from psychologists.models import PsychologistLanguage
from psychologists.serializers import PsyLanguageDynamicSerializer


class PsyLanguageListView(AdminOnlyView, ListView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/languages/psy_language_list.html'
    context_object_name = 'languages'


class PsyLanguageCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/languages/psy_language_create.html'
    form_class = PsyLanguageForm

    def get_success_url(self):
        return reverse('psy-language-create')


class PsyLanguageUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/languages/psy_language_update.html'
    form_class = PsyLanguageForm
    context_object_name = 'language'

    def get_success_url(self):
        return reverse('psy-language-update', kwargs={'pk': self.kwargs['pk']})


class PsyLanguageDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistLanguage
    template_name = 'cadmin/psychologists/languages/psy_language_delete.html'
    context_object_name = 'language'

    def get_success_url(self):
        return reverse('psy-language-list')


class PsyLanguageDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistLanguage
    form_class = PsyLanguageForm
    serializer_class = PsyLanguageDynamicSerializer
    template_name = 'cadmin/psychologists/languages/psy_language_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return self.save_form(request, form)

    def post(self, request):
        form = self.form_class(request.POST)
        return self.save_form(request, form)


class PsyLanguageDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistLanguage
    form_class = PsyLanguageForm
    serializer_class = PsyLanguageDynamicSerializer
    template_name = 'cadmin/psychologists/languages/psy_language_update_dynamic.html'

    def get(self, request, pk):
        language = get_object_or_404(PsychologistLanguage, pk=pk)
        form = self.form_class(instance=language)
        return self.save_form(request, form)

    def post(self, request, pk):
        language = get_object_or_404(PsychologistLanguage, pk=pk)
        form = self.form_class(request.POST, instance=language)
        return self.save_form(request, form)


class PsyLanguageDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistLanguage
    serializer_class = PsyLanguageDynamicSerializer
    template_name = 'cadmin/psychologists/languages/psy_language_delete_dynamic.html'
    forbidden_template_name = 'cadmin/psychologists/modal_403.html'

    def get(self, request, pk):
        language = get_object_or_404(PsychologistLanguage, pk=pk)
        return self.manage_delete(request, language)

    def post(self, request, pk):
        language = get_object_or_404(PsychologistLanguage, pk=pk)
        return self.manage_delete(request, language)
