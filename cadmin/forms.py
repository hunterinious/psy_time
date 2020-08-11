from django import forms
from psychologists.models import PsychologistUserProfile, PsychologistStatus


class PsychologistStatusForm(forms.ModelForm):
    profiles = forms.ModelMChoiceField(queryset=None)

    class Meta:
        model = PsychologistStatus
        fields = '__all__'
