from django.urls import reverse
from django.views.generic import (
    ListView,
    UpdateView,
)
from .core import AdminOnlyView
from cadmin.forms import HelpForm
from core.models import Help


class HelpRequestListView(AdminOnlyView, ListView):
    model = Help
    template_name = 'cadmin/help_requests/help_request_list.html'
    context_object_name = 'help_requests'


class HelpRequestUpdateView(AdminOnlyView, UpdateView):
    model = Help
    template_name = 'cadmin/help_requests/help_request_update.html'
    form_class = HelpForm
    context_object_name = 'help_request'

    def get_success_url(self):
        return reverse('help-request-update', kwargs={'pk': self.kwargs['pk']})
