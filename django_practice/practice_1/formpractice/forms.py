from django import forms
from formpractice.models import Student


def name_validate(value):
    if not value.isalpha():
        raise forms.ValidationError("Please Enter a valid name, Dont use Number in Name")
    return value

class StudentForm(forms.Form):


    name = forms.CharField(max_length=100,validators=[name_validate])
    email = forms.EmailField()
    age = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'date-input', 'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        help_text='Format: YYYY-MM-DD'
        )


    def __init__(self,*args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

