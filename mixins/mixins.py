from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.shortcuts import redirect
from users.models import UserTypes


class OnlyAdminCanAccessMixin(AccessMixin):
    """
    A view mixin that only allows admin users.
    """
    not_admin_message = ""
    not_admin_redirect = ""

    def get_not_admin_message(self):
        return self.not_admin_message

    def handle_not_admin(self):
        """ Deal with users that are not admins. """
        message = self.get_not_admin_message()
        if self.raise_exception:
            raise PermissionDenied(message)
        messages.error(self.request, message)
        return redirect(self.get_not_admin_redirect())

    def get_not_admin_redirect(self):
        """ Get the url name to redirect to if the user isn't admin. """

        if not self.not_admin_redirect:
            raise ImproperlyConfigured(
                '{0} is missing the not_admin_redirect attribute. Define {0}.not_admin_redirect, or override '
                '{0}.get_not_admin_redirect().'.format(self.__class__.__name__))
        return self.not_admin_redirect

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.handle_no_permission()
        if not user.user_type == UserTypes.admin_user.name:
            return self.handle_not_admin()
        return super().dispatch(request, *args, **kwargs)
