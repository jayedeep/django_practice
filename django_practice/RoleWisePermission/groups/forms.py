from django import forms
from .models import CustomGroup
class GroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = ['name','description']

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(UpdateGroupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        # self.fields['permissions'] = Permission.objects.filter()
