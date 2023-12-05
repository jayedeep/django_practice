from django import forms
from formpractice.models import Student

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
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
