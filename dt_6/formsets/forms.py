from django import forms
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from .models import Task, Author,Book


#base formset
class TaskForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={"cols": "10", "rows": "1",'class': 'form-control'}))

TaskFormset = formset_factory(TaskForm, extra=1,can_delete=True)

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields='__all__'

TaskModelFormset = modelformset_factory(model=Task,form=TaskModelForm,extra=2)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

BookFormSet = inlineformset_factory(Author, Book, fields=['title'])
