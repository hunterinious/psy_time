from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView, PsyDynamicOperationsView
from cadmin.forms import PsyFormatForm
from psychologists.models import PsychologistWorkFormat
from psychologists.serializers import PsyFormatDynamicSerializer


class PsyFormatListView(AdminOnlyView, ListView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/formats/psy_format_list.html'
    context_object_name = 'formats'


class PsyFormatCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/formats/psy_format_create.html'
    form_class = PsyFormatForm

    def get_success_url(self):
        return reverse('psy-format-create')


class PsyFormatUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/formats/psy_format_update.html'
    form_class = PsyFormatForm
    context_object_name = 'format'

    def get_success_url(self):
        return reverse('psy-format-update', kwargs={'pk': self.kwargs['pk']})


class PsyFormatDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistWorkFormat
    template_name = 'cadmin/psychologists/formats/psy_format_delete.html'
    context_object_name = 'format'

    def get_success_url(self):
        return reverse('psy-format-list')


class PsyFormatDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistWorkFormat
    form_class = PsyFormatForm
    serializer_class = PsyFormatDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return JsonResponse(self.save_form(form))

    def post(self, request):
        form = self.form_class(self.request.POST)
        return JsonResponse(self.save_form(form))


class PsyFormatDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistWorkFormat
    form_class = PsyFormatForm
    serializer_class = PsyFormatDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_update_dynamic.html'

    def get(self, request, pk):
        format = get_object_or_404(PsychologistWorkFormat, pk=pk)
        form = self.form_class(instance=format)
        return JsonResponse(self.save_form(form))

    def post(self, request, pk):
        format = get_object_or_404(PsychologistWorkFormat, pk=pk)
        form = self.form_class(request.POST, instance=format)
        return JsonResponse(self.save_form(form))


class PsyFormatDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistWorkFormat
    serializer_class = PsyFormatDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_delete_dynamic.html'

    def get(self, request, pk):
        format = get_object_or_404(PsychologistWorkFormat, pk=pk)
        return JsonResponse(self.manage_delete(format))

    def post(self, request, pk):
        format = get_object_or_404(PsychologistWorkFormat, pk=pk)
        return JsonResponse(self.manage_delete(format))
