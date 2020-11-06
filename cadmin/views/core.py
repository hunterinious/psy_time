from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    forbidden_delete_template_name = 'cadmin/modal_delete_403_refers_to_profiles.html'

    def save_form(self, form):
        data = dict()
        request = self.request
        instance_name = self.request.GET.get('instance_name')

        if request.POST and form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['data'] = self.serializer_class(self.model.objects.get_all(), many=True).data
        else:
            data['form_is_valid'] = False

        context = {'form': form, 'instance_name': instance_name}
        data['html_form'] = render_to_string(self.template_name, context, request=request)

        return data

    def manage_delete(self, obj):
        data = dict()
        request = self.request
        instance_name = self.request.GET.get('instance_name')
        template = self.template_name

        if request.POST:
            deleted = self.model.objects.delete_by_id(id=obj.id)

            if deleted:
                data['form_is_valid'] = True
                data['data'] = self.serializer_class(self.model.objects.get_all(), many=True).data
            else:
                template = self.forbidden_delete_template_name

        context = {'instance': obj, 'instance_name': instance_name}
        data['html_form'] = render_to_string(template, context, request=request)

        return data


class ModalChoiceView(AdminOnlyView):
    template_name = 'cadmin/modal_choice.html'

    def get(self, request):
        data = dict()
        data['html_form'] = render_to_string(self.template_name, request=request)
        return JsonResponse(data)
