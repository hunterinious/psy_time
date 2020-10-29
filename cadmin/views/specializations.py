from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView, PsyDynamicOperationsView
from cadmin.forms import PsySpecializationForm
from psychologists.models import PsychologistSpecialization
from psychologists.serializers import PsySpecializationDynamicSerializer


class PsySpecializationListView(AdminOnlyView, ListView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/specializations/psy_specialization_list.html'
    context_object_name = 'specializations'


class PsySpecializationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/specializations/psy_specialization_create.html'
    form_class = PsySpecializationForm

    def get_success_url(self):
        return reverse('psy-specialization-create')


class PsySpecializationUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/specializations/psy_specialization_update.html'
    form_class = PsySpecializationForm
    context_object_name = 'specialization'

    def get_success_url(self):
        return reverse('psy-specialization-update', kwargs={'pk': self.kwargs['pk']})


class PsySpecializationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistSpecialization
    template_name = 'cadmin/psychologists/specializations/psy_specialization_delete.html'
    context_object_name = 'specialization'

    def get_success_url(self):
        return reverse('psy-specialization-list')

class PsySpecializationDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistSpecialization
    form_class = PsySpecializationForm
    serializer_class = PsySpecializationDynamicSerializer
    template_name = 'cadmin/psychologists/specializations/psy_specialization_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return self.save_form(request, form)

    def post(self, request):
        form = self.form_class(request.POST)
        return self.save_form(request, form)


class PsySpecializationDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistSpecialization
    form_class = PsySpecializationForm
    serializer_class = PsySpecializationDynamicSerializer
    template_name = 'cadmin/psychologists/specializations/psy_specialization_update_dynamic.html'

    def get(self, request, pk):
        specialization = get_object_or_404(PsychologistSpecialization, pk=pk)
        form = self.form_class(instance=specialization)
        return self.save_form(request, form)

    def post(self, request, pk):
        specialization = get_object_or_404(PsychologistSpecialization, pk=pk)
        form = self.form_class(request.POST, instance=specialization)
        return self.save_form(request, form)


class PsySpecializationDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistSpecialization
    serializer_class = PsySpecializationDynamicSerializer
    template_name = 'cadmin/psychologists/specializations/psy_specialization_delete_dynamic.html'
    forbidden_template_name = 'cadmin/psychologists/modal_403.html'

    def get(self, request, pk):
        specialization = get_object_or_404(PsychologistSpecialization, pk=pk)
        return self.manage_delete(request, specialization)

    def post(self, request, pk):
        specialization = get_object_or_404(PsychologistSpecialization, pk=pk)
        return self.manage_delete(request, specialization)
