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
from cadmin.forms import PsyEducationForm
from psychologists.models import PsychologistEducation
from psychologists.serializers import PsyEducationDynamicSerializer


class PsyEducationListView(AdminOnlyView, ListView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/educations/psy_education_list.html'
    context_object_name = 'educations'


class PsyEducationCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/psychologists/educations/psy_education_create.html'
    form_class = PsyEducationForm

    def get_success_url(self):
        return reverse('psy-education-create')


class PsyEducationUpdateView(AdminOnlyView, UpdateView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/educations/psy_education_update.html'
    form_class = PsyEducationForm
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('psy-education-update', kwargs={'pk': self.kwargs['pk']})


class PsyEducationDeleteView(AdminOnlyView, DeleteView):
    model = PsychologistEducation
    template_name = 'cadmin/psychologists/educations/psy_education_delete.html'
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('psy-education-list')


class PsyEducationDynamicCreateView(PsyDynamicOperationsView):
    model = PsychologistEducation
    form_class = PsyEducationForm
    serializer_class = PsyEducationDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_create_dynamic.html'

    def get(self, request):
        form = self.form_class()
        return JsonResponse(self.save_form(form))

    def post(self, request):
        form = self.form_class(self.request.POST)
        return JsonResponse(self.save_form(form))


class PsyEducationDynamicUpdateView(PsyDynamicOperationsView):
    model = PsychologistEducation
    form_class = PsyEducationForm
    serializer_class = PsyEducationDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_update_dynamic.html'

    def get(self, request, pk):
        education = get_object_or_404(PsychologistEducation, pk=pk)
        form = self.form_class(instance=education)
        return JsonResponse(self.save_form(form))

    def post(self, request, pk):
        education = get_object_or_404(PsychologistEducation, pk=pk)
        form = self.form_class(request.POST, instance=education)
        return JsonResponse(self.save_form(form))


class PsyEducationDynamicDeleteView(PsyDynamicOperationsView):
    model = PsychologistEducation
    serializer_class = PsyEducationDynamicSerializer
    template_name = 'cadmin/psychologists/psy_related_model_delete_dynamic.html'
    forbidden_template_name = 'cadmin/modal_403_refers_to_profiles.html'

    def get(self, request, pk):
        education = get_object_or_404(PsychologistEducation, pk=pk)
        return JsonResponse(self.manage_delete(education))

    def post(self, request, pk):
        education = get_object_or_404(PsychologistEducation, pk=pk)
        return JsonResponse(self.manage_delete(education))
