from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model
from django.urls import reverse
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


class CustomSelect(forms.SelectMultiple):
    def __init__(self, *args, **kwargs):
        self.set = kwargs.pop('set')
        super(CustomSelect, self).__init__(*args, **kwargs)

    def create_option(
            self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        if value:
            option['attrs'].update({
                'data-url': reverse(f'psy-{self.set}-update-dynamic', kwargs={'pk': value}),
                'delete-url': reverse(f'psy-{self.set}-delete-dynamic', kwargs={'pk': value})
            })
        return option


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


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'user_type')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'user_type')


class PsyProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistUserProfile
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(),
            'statuses': CustomSelect(set='status', attrs={'size': 10}),
            'approaches': CustomSelect(set='approach', attrs={'size': 10}),
            'specializations': CustomSelect(set='specialization', attrs={'size': 10}),
            'formats': CustomSelect(set='format', attrs={'size': 10}),
            'themes': CustomSelect(set='theme', attrs={'size': 10}),
            'educations': CustomSelect(set='education', attrs={'size': 10}),
            'secondary_educations': CustomSelect(set='secondary-education', attrs={'size': 10}),
            'languages': CustomSelect(set='language', attrs={'size': 10})
        }


PsyProfileFormSet = inlineformset_factory(PsychologistUser, PsychologistUserProfile,
                                          form=PsyProfileForm, can_delete=False)


class PsyStatusForm(forms.ModelForm):
    class Meta:
        model = PsychologistStatus
        fields = '__all__'


class PsyApproachForm(forms.ModelForm):
    class Meta:
        model = PsychologistApproach
        fields = '__all__'


class PsySpecializationForm(forms.ModelForm):
    class Meta:
        model = PsychologistSpecialization
        fields = '__all__'


class PsyFormatForm(forms.ModelForm):
    class Meta:
        model = PsychologistWorkFormat
        fields = '__all__'


class PsyThemeForm(forms.ModelForm):
    class Meta:
        model = PsychologistTheme
        fields = '__all__'


class PsyEducationForm(forms.ModelForm):
    class Meta:
        model = PsychologistEducation
        fields = '__all__'


class PsySecondaryEducationForm(forms.ModelForm):
    class Meta:
        model = PsychologistSecondaryEducation
        fields = '__all__'


class PsyLanguageForm(forms.ModelForm):
    class Meta:
        model = PsychologistLanguage
        fields = '__all__'


class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HelpForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            if key != 'status':
                self.fields[key].widget.attrs['readonly'] = True
