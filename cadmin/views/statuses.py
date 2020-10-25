from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import PsychologistStatusForm
from psychologists.models import PsychologistStatus
from psychologists.serializers import PsyStatusDynamicSerializer


class PsychologistStatusListView(AdminOnlyView, ListView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/psy_status_list.html'
    context_object_name = 'statuses'


class PsychologistStatusCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/psy_status_create.html'
    form_class = PsychologistStatusForm

    def get_success_url(self):
        return reverse('psy-status-create')


class PsychologistStatusUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/psy_status_update.html'
    form_class = PsychologistStatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('psy-status-update', kwargs={'pk': self.kwargs['pk']})


class PsychologistStatusDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistStatus
    template_name = 'cadmin/psychologists/psy_status_delete.html'
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('psy-status-list')


class PsyDynamicOperationsView(AdminOnlyView, View):
    model = None
    form_class = None
    serializer_class = None
    template_name = None
    forbidden_template_name = None

    def save_form(self, request, form):
        data = dict()

        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['data'] = self.serializer_class(self.model.objects.get_all(), many=True).data
        else:
            data['form_is_valid'] = False

        context = {'form': form}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)

    def manage_delete(self, request, obj):
        data = dict()
        template = self.template_name

        if request.POST:
            deleted = self.model.objects.delete_by_name(name=obj.name)

            if deleted:
                data['form_is_valid'] = True
                data['data'] = self.serializer_class(self.model.objects.get_all(), many=True).data
            else:
                template = self.forbidden_template_name

        context = {'instance': obj}
        data['html_form'] = render_to_string(template, context, request=request)

        return JsonResponse(data)


class PsychologistStatusDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistStatus
    form_class = PsychologistStatusForm
    serializer_class = PsyStatusDynamicSerializer
    template_name = 'cadmin/psychologists/psy_status_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return self.save_form(request, form)

    def post(self, request):
        form = self.form_class(request.POST)
        return self.save_form(request, form)


class PsychologistStatusDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistStatus
    form_class = PsychologistStatusForm
    serializer_class = PsyStatusDynamicSerializer
    template_name = 'cadmin/psychologists/psy_status_update_dynamic.html'

    def get(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        form = self.form_class(instance=status)
        return self.save_form(request, form)

    def post(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        form = self.form_class(request.POST, instance=status)
        return self.save_form(request, form)


class PsychologistStatusDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistStatus
    serializer_class = PsyStatusDynamicSerializer
    template_name = 'cadmin/psychologists/psy_status_delete_dynamic.html'
    forbidden_template_name = 'cadmin/psychologists/modal_403.html'

    def get(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        return self.manage_delete(request, status)

    def post(self, request, pk):
        status = get_object_or_404(PsychologistStatus, pk=pk)
        return self.manage_delete(request, status)
