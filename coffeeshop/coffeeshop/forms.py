from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset

from . import models
from .widgets import PlaceholderInput, ShowHidePasswordWidget

class NameForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    
    def save(self):
        pass



class Signup(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'signup'
        self.helper.add_input(Submit('submit', 'Sign up', css_class='btn-success'))

        self.helper.layout = Layout(Fieldset('User Information', 'username', 'password', style='color:green;'),
            Fieldset('Contact data', 'email', style='color: green;'))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        error_messages = {
            'username':{
                'unique': _('Please enter another username, This one is taken'),
            }
        }

        widgets = {
            'username': PlaceholderInput, #forms.TextInput(attrs={'placeholder':'Username'}),
            'password': ShowHidePasswordWidget,
        }

    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m


class UserDetailsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userDetailsForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'signup'
        self.helper.add_input(Submit('submit', 'Sign Up', css_class='btn-success'))

        self.helper.layout = Layout(
            Fieldset('Name', 'username', 'first_name', 'last_name', style='color:grey;'),
            Fieldset('Contact data', 'email', 'phone', style='color:grey;'),
            Fieldset("Address details", 'address', 'zip_code', style='color:grey;')

        )

    class Meta:
        model = models.UserDetails
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'address', 'zip_code']
        error_messages = {
            'zip_code': {
                'invalid': _('Zip code should be in the form 00000 or 00000-0000'),
            }
        }

        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }

"""     def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')
        if len(zip_code) not in (5,10):
            raise forms.ValidationError('Zip code should be in form 00000 or 00000-0000')
        return zip_code """