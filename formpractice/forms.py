from django import forms
from formpractice.models import Student

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = ['name','email','age']