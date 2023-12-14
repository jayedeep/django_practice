from django.shortcuts import render,redirect,get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from django.contrib import messages


# Create your views here.
def home(request):
    form = TeacherForm()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher record inserted.")
            return redirect('home')
        else:
            messages.error(request, "Got error on Create new record.")
    return render(request, 'modelformpractice/home.html',{'teachers':teachers,'form':form})


def single_teacher(request,id):
    teacher = get_object_or_404(Teacher,id=id)
    return render(request, 'modelformpractice/single_teacher.html',{'teacher':teacher})

def single_teacher_update(request,id):
    teacher = get_object_or_404(Teacher,id=id)
    teacher_form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST,instance=teacher)
        if teacher_form.is_valid():
            teacher_form.save()
            messages.success(request, "Teacher record updated.")
            return redirect('home')
        else:
            messages.error(request, "Got error on Update record.")
    return render(request, 'modelformpractice/single_teacher_update.html',{'teacher_form':teacher_form})

def teacher_delete(request,id):
    teachers = Teacher.objects.filter(id=id)
    teachers.delete()
    messages.success(request, "Teacher record deleted.")
    return redirect('home')
