from django import forms
from django.forms.widgets import Widget
from django.forms.utils import flatatt

class MySelectWidget(Widget):
    def __init__(self, choices=(), attrs=None):
        print('attrs.',attrs)
        super().__init__(attrs)
        self.choices = choices

    def render(self, name, value, attrs=None, renderer=None):
        options = []
        for choice_value, choice_label in self.choices:
            selected = ''
            if value == choice_value:
                selected = 'selected'
            option_html = f'<option value="{choice_value}" {selected}>{choice_label}</option>'
            options.append(option_html)
        select_html = '<select class="form-control" name="{}"{}>{}</select>'.format(name, flatatt(attrs), '\n'.join(options))
        return select_html

    def value_from_datadict(self, data, files, name):
        return data.get(name, None)