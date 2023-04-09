from cProfile import label

from django import forms
from django.core.exceptions import ValidationError

from .models import Student
from .custom_widgets import MySelectWidget


def custom_validator(value):
    if len(value.split(' '))>1:
        raise ValidationError('Please enter only one word')

class StudentForm(forms.ModelForm):

    states = [('gujarat','Gujarat'),('rajsthan','Rajsthan'),('maharastra','Maharastra')]
    name = forms.CharField(validators=[custom_validator],widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=states,widget=MySelectWidget(attrs={'class': 'form-control custom-class'}))
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
            # 'state': MySelectWidget(attrs={'class': 'form-control custom-class'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('.com'):
            raise ValidationError('Invalid email address')
        return email

    def clean(self):
        cleaned_data = super().clean()
        if Student.objects.filter(name=cleaned_data.get('name')):
            raise ValidationError({'name':'Name already in use, Please Try Again'})

    def save(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        state = self.cleaned_data['state']
        # do something with the name and email
        # for example, save them to the database
        print('name',name,'email',email,'phone',phone)
        user = Student(name=name, email=email,phone=phone,state=state)
        user.save()
        return user