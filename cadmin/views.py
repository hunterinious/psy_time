from django.urls import reverse
from django.views.generic import CreateView
from .forms import PsychologistStatusForm


class PsychologistStatusCreateView(CreateView):
    template_name = 'cadmin/psy_status_create.html'
    form_class = PsychologistStatusForm

    def get_success_url(self):
        return reverse('psy-status-create')