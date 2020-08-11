from django import forms
from psychologists.models import PsychologistUserProfile, PsychologistStatus


class PsychologistStatusForm(forms.ModelForm):
    profiles = forms.ModelMultipleChoiceField(PsychologistUserProfile.objects.all(), required=False)

    class Meta:
        model = PsychologistStatus
        fields = '__all__'
