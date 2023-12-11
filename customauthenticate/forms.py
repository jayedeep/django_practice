from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Code
User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User

    def __init__(self,*args,**kwargs):
        super(CustomAuthenticationForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','phone_number','password','confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','phone_number']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        print(">>>kwargs\n\n\n\n",kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['code']

    def __init__(self, *args, **kwargs):
        super(CodeForm, self).__init__(*args, **kwargs)
        print(">>>kwargs\n\n\n\n",kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_fields = super().clean()
        code = cleaned_fields.get('code')
        if self.instance and self.instance.code != code:
            forms.ValidationError("Varification Code no matched")
        return cleaned_fields