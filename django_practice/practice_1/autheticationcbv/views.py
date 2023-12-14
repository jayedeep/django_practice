from django.shortcuts import render
from django.views.generic import FormView
from .forms import RegisterForm

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        print(">>>>>>>>form",form)
        form.save()
        form = super(RegisterView, self).form_valid(form)
        print("><<<<<",form)
        return form

