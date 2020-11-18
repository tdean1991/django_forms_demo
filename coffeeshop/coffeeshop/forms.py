from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from . import models

class NameForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    
    def save(self):
        pass



class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        error_messages = {
            'username':{
                'unique': _('Please enter another username, This one is taken'),
            }
        }

    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = models.UserDetails
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'address', 'zip_code']
        error_messages = {
            'zip_code': {
                'invalid': _('Zip code should be in the form 00000 or 00000-0000'),
            }
        }

"""     def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')
        if len(zip_code) not in (5,10):
            raise forms.ValidationError('Zip code should be in form 00000 or 00000-0000')
        return zip_code """