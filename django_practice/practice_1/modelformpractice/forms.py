from django import forms
from modelformpractice.models import Teacher


def name_validate(value):
    if not value.isalpha():
        raise forms.ValidationError("Please Enter a valid name, Dont use Number in Name")
    return value

class TeacherForm(forms.ModelForm):
    bod = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'date-input', 'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        help_text='Format: YYYY-MM-DD'
        )
    class Meta:
        model = Teacher
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

