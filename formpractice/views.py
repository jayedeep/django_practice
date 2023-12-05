from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages


# Create your views here.
def home(request):
    form = StudentForm()
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            student = Student.objects.create(name=name, email=email, age=age)
            messages.success(request, "Student record inserted.")
            return redirect('home')
        else:
            messages.error(request, "Got error on Create new record.")
    return render(request, 'formpractice/home.html',{'students':students,'form':form})


def single_student(request,id):
    student = get_object_or_404(Student,id=id)
    return render(request, 'formpractice/single_student.html',{'student':student})

def single_student_update(request,id):
    student = get_object_or_404(Student,id=id)
    student_form = StudentForm(initial={'name':student.name,'email':student.email,'age':student.age})
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.name=form.cleaned_data['name']
            student.email=form.cleaned_data['email']
            student.age=form.cleaned_data['age']
            student.save()
            messages.success(request, "Student record updated.")
            return redirect('home')
        else:
            messages.error(request, "Got error on Update record.")
    return render(request, 'formpractice/single_student_update.html',{'student_form':student_form})

def student_delete(request,id):
    students = Student.objects.filter(id=id)
    students.delete()
    messages.success(request, "Student record deleted.")
    return redirect('home')
