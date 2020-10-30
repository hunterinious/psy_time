from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView

User = get_user_model()


class AdminOnlyView(LoginRequiredMixin, UserPassesTestMixin, View):
    permission_denied_message = 'Only admin has access to this view'

    def test_func(self):
        return self.request.user.user_type == User.UserTypes.ADMIN_USER


class MainAdminView(AdminOnlyView, TemplateView):
    template_name = 'cadmin/index.html'


class PsyDynamicOperationsView(AdminOnlyView):
    model = None
    form_class = None
    serializer_class = None
    template_name = None
    forbidden_template_name = None

    def save_form(self, request, form):
        data = dict()

        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['data'] = self.serializer_class(self.model.objects.get_all(), many=True).data
        else:
            data['form_is_valid'] = False

        context = {'form': form}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)

    def manage_delete(self, request, obj):
        data = dict()
        template = self.template_name

        if request.POST:
            deleted = self.model.objects.delete_by_name(name=obj.name)

            if deleted:
                data['form_is_valid'] = True
                data['data'] = self.serializer_class(self.model.objects.get_all(), many=True).data
            else:
                template = self.forbidden_template_name

        context = {'instance': obj}
        data['html_form'] = render_to_string(template, context, request=request)

        return JsonResponse(data)


class ModalChoiceView(AdminOnlyView):
    template_name = 'cadmin/psychologists/modal_choice.html'

    def get(self, request):
        data = dict()
        data['html_form'] = render_to_string(self.template_name, request=request)
        return JsonResponse(data)
