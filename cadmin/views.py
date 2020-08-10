from django.urls import reverse
from django.views.generic import CreateView
from .forms import PsychologistProfileForm


class PsychologistProfileCreateView(CreateView):
    template_name = 'cadmin/psy_profile_create.html'
    form_class = PsychologistProfileForm

    def get_success_url(self):
        return reverse('psy-profile-create')