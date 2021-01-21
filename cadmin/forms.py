from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model
from django.urls import reverse
from psychologists.models import PsychologistUser
from locations.models import Country, City, Timezone
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
from django_select2 import forms as s2forms

User = get_user_model()


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomBaseSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        self.set = kwargs.pop('set')
        super(CustomBaseSelect, self).__init__(*args, **kwargs)

    def create_option(
            self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        if value:
            option['attrs'].update({
                'data-url': reverse(f'{self.set}-update-dynamic', kwargs={'pk': value}),
                'delete-url': reverse(f'{self.set}-delete-dynamic', kwargs={'pk': value})
            })
        return option


class CustomMultipleSelect(CustomBaseSelect, forms.SelectMultiple):
    pass


class CustomSelect(CustomBaseSelect, s2forms.Select2Widget):
    pass


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Country name"


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "City name"


CityFormSet = inlineformset_factory(Country, City,
                                    form=CityForm, can_delete=False, max_num=1)


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'user_type')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'user_type')


class PsyProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistUserProfile
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(),
            'statuses': CustomMultipleSelect(set='psy-status', attrs={'size': 10}),
            'approaches': CustomMultipleSelect(set='psy-approach', attrs={'size': 10}),
            'specializations': CustomMultipleSelect(set='psy-specialization', attrs={'size': 10}),
            'formats': CustomMultipleSelect(set='psy-format', attrs={'size': 10}),
            'themes': CustomMultipleSelect(set='psy-theme', attrs={'size': 10}),
            'educations': CustomMultipleSelect(set='psy-education', attrs={'size': 10}),
            'secondary_educations': CustomMultipleSelect(set='psy-secondary-education', attrs={'size': 10}),
            'languages': CustomMultipleSelect(set='psy-language', attrs={'size': 10}),
            'city': CustomSelect(set='city'),
            'timezone': s2forms.Select2Widget()
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
