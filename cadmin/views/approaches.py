from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView, PsyDynamicOperationsView
from cadmin.forms import PsyApproachForm
from psychologists.models import PsychologistApproach
from psychologists.serializers import PsyApproachDynamicSerializer


class PsyApproachListView(AdminOnlyView, ListView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/approaches/psy_approach_list.html'
    context_object_name = 'approaches'


class PsyApproachCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/approaches/psy_approach_create_dynamic.html'
    form_class = PsyApproachForm

    def get_success_url(self):
        return reverse('psy-approach-create')


class PsyApproachUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/approaches/psy_approach_update_dynamic.html'
    form_class = PsyApproachForm
    context_object_name = 'approach'

    def get_success_url(self):
        return reverse('psy-approach-update', kwargs={'pk': self.kwargs['pk']})


class PsyApproachDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistApproach
    template_name = 'cadmin/psychologists/approaches/psy_approach_delete.html'
    context_object_name = 'approach'

    def get_success_url(self):
        return reverse('psy-approach-list')


class PsyApproachDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistApproach
    form_class = PsyApproachForm
    serializer_class = PsyApproachDynamicSerializer
    template_name = 'cadmin/psychologists/approaches/psy_approach_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return self.save_form(request, form)

    def post(self, request):
        form = self.form_class(request.POST)
        return self.save_form(request, form)


class PsyApproachDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistApproach
    form_class = PsyApproachForm
    serializer_class = PsyApproachDynamicSerializer
    template_name = 'cadmin/psychologists/approaches/psy_approach_update_dynamic.html'

    def get(self, request, pk):
        approach = get_object_or_404(PsychologistApproach, pk=pk)
        form = self.form_class(instance=approach)
        return self.save_form(request, form)

    def post(self, request, pk):
        approach = get_object_or_404(PsychologistApproach, pk=pk)
        form = self.form_class(request.POST, instance=approach)
        return self.save_form(request, form)


class PsyApproachDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistApproach
    serializer_class = PsyApproachDynamicSerializer
    template_name = 'cadmin/psychologists/approaches/psy_approach_delete_dynamic.html'
    forbidden_template_name = 'cadmin/modal_403_refers_to_profiles.html'

    def get(self, request, pk):
        approach = get_object_or_404(PsychologistApproach, pk=pk)
        return self.manage_delete(request, approach)

    def post(self, request, pk):
        approach = get_object_or_404(PsychologistApproach, pk=pk)
        return self.manage_delete(request, approach)