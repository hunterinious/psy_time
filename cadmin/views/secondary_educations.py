from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .core import AdminOnlyView, PsyDynamicOperationsView
from cadmin.forms import PsySecondaryEducationForm
from psychologists.models import PsychologistSecondaryEducation
from psychologists.serializers import PsySecondaryEducationDynamicSerializer


class PsySecondaryEducationListView(AdminOnlyView, ListView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_list.html'
    context_object_name = 'secondary_educations'


class PsySecondaryEducationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_create.html'
    form_class = PsySecondaryEducationForm

    def get_success_url(self):
        return reverse('psy-secondary-education-create')


class PsySecondaryEducationUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_update.html'
    form_class = PsySecondaryEducationForm
    context_object_name = 'secondary_education'

    def get_success_url(self):
        return reverse('psy-secondary-education-update', kwargs={'pk': self.kwargs['pk']})


class PsySecondaryEducationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistSecondaryEducation
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_delete.html'
    context_object_name = 'secondary_education'

    def get_success_url(self):
        return reverse('psy-secondary-education-list')


class PsySecondaryEducationDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistSecondaryEducation
    form_class = PsySecondaryEducationForm
    serializer_class = PsySecondaryEducationDynamicSerializer
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return self.save_form(request, form)

    def post(self, request):
        form = self.form_class(request.POST)
        return self.save_form(request, form)


class PsySecondaryEducationDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistSecondaryEducation
    form_class = PsySecondaryEducationForm
    serializer_class = PsySecondaryEducationDynamicSerializer
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_update_dynamic.html'

    def get(self, request, pk):
        secondary_education = get_object_or_404(PsychologistSecondaryEducation, pk=pk)
        form = self.form_class(instance=secondary_education)
        return self.save_form(request, form)

    def post(self, request, pk):
        secondary_education = get_object_or_404(PsychologistSecondaryEducation, pk=pk)
        form = self.form_class(request.POST, instance=secondary_education)
        return self.save_form(request, form)


class PsySecondaryEducationDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistSecondaryEducation
    serializer_class = PsySecondaryEducationDynamicSerializer
    template_name = 'cadmin/psychologists/secondary_educations/psy_secondary_education_delete_dynamic.html'
    forbidden_template_name = 'cadmin/modal_403_refers_to_profiles.html'

    def get(self, request, pk):
        secondary_education = get_object_or_404(PsychologistSecondaryEducation, pk=pk)
        return self.manage_delete(request, secondary_education)

    def post(self, request, pk):
        secondary_education = get_object_or_404(PsychologistSecondaryEducation, pk=pk)
        return self.manage_delete(request, secondary_education)
