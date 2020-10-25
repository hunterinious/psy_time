from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
)
from .core import AdminOnlyView
from cadmin.forms import UserForm


User = get_user_model()


class UserCreateView(AdminOnlyView, CreateView):
    template_name = 'cadmin/users/user_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user-create')


class UserDeleteView(AdminOnlyView, DeleteView):
    model = User
    template_name = 'cadmin/users/user_delete.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('user-delete')


class PsychologistUserListView(AdminOnlyView, ListView):
    template_name = 'cadmin/psychologists/psy_list.html'
    context_object_name = 'psychologists'

    def get_queryset(self):
        return User.objects.get_psychologists_users()
