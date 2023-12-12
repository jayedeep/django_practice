from django import forms
from .models import Roles
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['role_name']

    def __init__(self, *args, **kwargs):
        super(RolesForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-select"


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

    def __init__(self, *args, **kwargs):
        super(FacultyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
