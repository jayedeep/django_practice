from django.shortcuts import render,redirect

from .forms import StudentForm


# Create your views here.

def index(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_form')
        else:
            print(form.errors)
    return render(request, 'index.html',{'form':form})