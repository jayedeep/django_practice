from django import forms

from firstthreetopics.models import Student, Character


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'date_of_birth']
    # use below to set default date set into date field.
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'date-input','type': 'date'}),
        input_formats=['%Y-%m-%d'],
        help_text='Format: YYYY-MM-DD'
    )
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class CharacterForm(forms.Form):
    character_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))




