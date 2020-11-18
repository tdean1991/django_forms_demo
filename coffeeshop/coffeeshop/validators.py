import django.forms as forms

def validate_zipcode(value):
    if len(value) not in (5,10):
        raise forms.ValidationError('Zip code should be in form 00000 or 00000-0000',
                    code='invalid',
                    params={'value':value},
                    )
        