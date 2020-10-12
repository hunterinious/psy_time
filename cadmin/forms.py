from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model
from psychologists.models import PsychologistUser
from locations.models import Country, City
from psychologists.models import (
    PsychologistUserProfile,
    PsychologistStatus,
    PsychologistApproach,
    PsychologistSpecialization,
    PsychologistWorkFormat,
    PsychologistTheme,
    PsychologistEducation,
    PsychologistSecondaryEducation,
    PsychologistLanguage,
)
from core.models import Help

User = get_user_model()


class DateInput(forms.DateInput):
    input_type = 'date'


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'user_type')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class PsychologistProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistUserProfile
        fields = '__all__'
        widgets = {
            'birth_date': DateInput()
        }


PsychologistProfileFormSet = inlineformset_factory(PsychologistUser, PsychologistUserProfile,
                                                   form=PsychologistProfileForm, can_delete=False)


class PsychologistStatusForm(forms.ModelForm):
    class Meta:
        model = PsychologistStatus
        fields = '__all__'


class PsychologistApproachForm(forms.ModelForm):
    class Meta:
        model = PsychologistApproach
        fields = '__all__'


class PsychologistSpecializationForm(forms.ModelForm):
    class Meta:
        model = PsychologistSpecialization
        fields = '__all__'


class PsychologistFormatForm(forms.ModelForm):
    class Meta:
        model = PsychologistWorkFormat
        fields = '__all__'


class PsychologistThemeForm(forms.ModelForm):
    class Meta:
        model = PsychologistTheme
        fields = '__all__'


class PsychologistEducationForm(forms.ModelForm):
    class Meta:
        model = PsychologistEducation
        fields = '__all__'


class PsychologistSecondaryEducationForm(forms.ModelForm):
    class Meta:
        model = PsychologistSecondaryEducation
        fields = '__all__'


class PsychologistLanguageForm(forms.ModelForm):
    class Meta:
        model = PsychologistLanguage
        fields = '__all__'


import logging
logger = logging.getLogger(__name__)
class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HelpForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            if key != 'status':
                self.fields[key].widget.attrs['readonly'] = True
