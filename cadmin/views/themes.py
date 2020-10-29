from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView, PsyDynamicOperationsView
from cadmin.forms import PsyThemeForm
from psychologists.models import PsychologistTheme
from psychologists.serializers import PsyThemeDynamicSerializer


class PsyThemeListView(AdminOnlyView, ListView):
    model = PsychologistTheme
    template_name = 'cadmin/psychologists/themes/psy_theme_list.html'
    context_object_name = 'themes'


class PsyThemeCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/themes/psy_theme_create.html'
    form_class = PsyThemeForm

    def get_success_url(self):
        return reverse('psy-theme-create')


class PsyThemeUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistTheme
    template_name = 'cadmin/psychologists/themes/psy_theme_update.html'
    form_class = PsyThemeForm
    context_object_name = 'theme'

    def get_success_url(self):
        return reverse('psy-theme-update', kwargs={'pk': self.kwargs['pk']})


class PsyThemeDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistTheme
    template_name = 'cadmin/psychologists/themes/psy_theme_delete.html'
    context_object_name = 'theme'

    def get_success_url(self):
        return reverse('psy-theme-list')
    
    
class PsyThemeDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistTheme
    form_class = PsyThemeForm
    serializer_class = PsyThemeDynamicSerializer
    template_name = 'cadmin/psychologists/themes/psy_theme_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return self.save_form(request, form)

    def post(self, request):
        form = self.form_class(request.POST)
        return self.save_form(request, form)


class PsyThemeDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistTheme
    form_class = PsyThemeForm
    serializer_class = PsyThemeDynamicSerializer
    template_name = 'cadmin/psychologists/themes/psy_theme_update_dynamic.html'

    def get(self, request, pk):
        theme = get_object_or_404(PsychologistTheme, pk=pk)
        form = self.form_class(instance=theme)
        return self.save_form(request, form)

    def post(self, request, pk):
        theme = get_object_or_404(PsychologistTheme, pk=pk)
        form = self.form_class(request.POST, instance=theme)
        return self.save_form(request, form)


class PsyThemeDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistTheme
    serializer_class = PsyThemeDynamicSerializer
    template_name = 'cadmin/psychologists/themes/psy_theme_delete_dynamic.html'
    forbidden_template_name = 'cadmin/psychologists/modal_403.html'

    def get(self, request, pk):
        theme = get_object_or_404(PsychologistTheme, pk=pk)
        return self.manage_delete(request, theme)

    def post(self, request, pk):
        theme = get_object_or_404(PsychologistTheme, pk=pk)
        return self.manage_delete(request, theme)
