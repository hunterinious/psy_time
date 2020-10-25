from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views import View
from django.views.generic import TemplateView

User = get_user_model()


class AdminOnlyView(LoginRequiredMixin, UserPassesTestMixin, View):
    permission_denied_message = 'Only admin has access to this view'

    def test_func(self):
        return self.request.user.user_type == User.UserTypes.ADMIN_USER


class MainAdminView(AdminOnlyView, TemplateView):
    template_name = 'cadmin/index.html'
