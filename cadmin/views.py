from django.urls import reverse
from django.views.generic import CreateView
from .forms import UserForm


class UserCreateView(CreateView):
    template_name = 'cadmin/user_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user-create')
