from django import forms
from django.contrib.auth import get_user_model
from psychologists.models import PsychologistUserProfile


class DateInput(forms.DateInput):
    input_type = 'date'


class PsychologistProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistUserProfile
        fields = '__all__'
        widgets = {
            'birth_date': DateInput()
        }
