from django import forms
from django.forms.utils import flatatt
from django.utils.html import mark_safe

class PlaceholderInput(forms.widgets.Input):
    input_type = 'text'
    template_name = 'coffeeshop/widgets/placeholder.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['maxlength'] = 30
        return context

class ShowHidePasswordWidget(forms.PasswordInput):
    class Media:
        js = ('script.js',)

    
    def render(self, name, value, attrs=None, **kwargs):
        final_attrs = self.build_attrs(attrs)
        output = self.get_template(final_attrs, value)
        return mark_safe(output)

    
    def get_template(self, attrs, value):
        flat_attrs = flatatt(attrs)
        return (
            '''
                <input %(attrs)s name="password" type="password" value="%(value)s" />
                <span id="__action__%(id)s__show_button">
                    <a href="javascript:show_pwd()">Show</a></span>
                <span id="__action__%(id)s__hide_button" style="display:none;">
                    <a href="javascript:hide_pwd()">Hide</a></span>
                
            ''') % {
                'attrs':flat_attrs,
                'id':attrs['id'],
                'value': value,
            }
        
