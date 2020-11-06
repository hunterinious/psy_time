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
from cadmin.forms import PsyStatusForm
from psychologists.models import PsychologistStatus
from psychologists.serializers import PsyStatusDynamicSerializer


class PsyStatusListView(AdminOnlyView, ListView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/statuses/psy_status_list.html'
    context_object_name = 'statuses'


class PsyStatusCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/statuses/psy_status_create.html'
    form_class = PsyStatusForm

    def get_success_url(self):
        return reverse('psy-status-create')


class PsyStatusUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/statuses/psy_status_update.html'
    form_class = PsyStatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('psy-status-update', kwargs={'pk': self.kwargs['pk']})


class PsyStatusDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/statuses/psy_status_delete.html'
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('psy-status-list')


class PsyStatusDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistStatus
    form_class = PsyStatusForm
    serializer_class = PsyStatusDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return JsonResponse(self.save_form(form))

    def post(self, request):
        form = self.form_class(self.request.POST)
        return JsonResponse(self.save_form(form))


class PsyStatusDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistStatus
    form_class = PsyStatusForm
    serializer_class = PsyStatusDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_update_dynamic.html'

    def get(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        form = self.form_class(instance=status)
        return JsonResponse(self.save_form(form))

    def post(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        form = self.form_class(request.POST, instance=status)
        return JsonResponse(self.save_form(form))


class PsyStatusDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistStatus
    serializer_class = PsyStatusDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_delete_dynamic.html'

    def get(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        return JsonResponse(self.manage_delete(status))

    def post(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        return JsonResponse(self.manage_delete(status))
