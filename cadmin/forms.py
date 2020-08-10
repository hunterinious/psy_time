from django import forms
from django.contrib.auth import get_user_model
from users.models import CustomUser

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'user_type')