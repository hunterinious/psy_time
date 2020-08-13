from django import forms
from django.contrib.auth import get_user_model
from users.models import CustomUser
from locations.models import Country, City
from psychologists.models import (
    PsychologistUserProfile,
    PsychologistStatus,
    PsychologistApproach,
    PsychologistSpecialization,
)

User = get_user_model()


class DateInput(forms.DateInput):
    input_type = 'date'


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


class PsychologistProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistUserProfile
        fields = '__all__'
        widgets = {
            'birth_date': DateInput()
        }


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

