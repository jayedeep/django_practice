from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.list import ListView
from firstthreetopics.forms import StudentForm, CharacterForm
from firstthreetopics.models import Student, Character
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView): # to render home page as templateview
    template_name = 'home.html'

    def get_context_data(self,**kwargs):  # used to custom context pass to template
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['header_name'] = 'Mystic Falls Students'
        student_form = StudentForm()
        character_form = CharacterForm()
        context['student_form'] = student_form
        context['character_form'] = character_form

        context['students'] = Student.objects.all()
        return context

    def post(self,request):  #  TemplateView  have already inherited View class so have get,post,...
        student_form = StudentForm(request.POST)
        character_form = CharacterForm()
        if student_form.is_valid():
            student = student_form.save()
            Character.objects.create(student=student,name = request.POST.get('character_name'))
            return redirect('home')
        else:
            print(">>>>>student_form",student_form.errors)
        return render(request, 'student_form.html', {'student_form': student_form,
                                                     'character_form': character_form,
                                                     'header_name': "Update Student"})


class StudentUpdate(TemplateView):
    def get(self,request,pk):
        student = Student.objects.get(pk=pk)
        # pass to set inital date into update form
        student_form = StudentForm(instance = student,initial={'date_of_birth':student.date_of_birth})
        character_form = CharacterForm(initial = {'character_name':student.character_set.first().name})
        return render(request,'student_form.html',{'student_form':student_form,
                                                    'character_form':character_form,
                                                   'header_name':"Update Student"})
    def post(self,request,pk):
        student = Student.objects.get(pk=pk)
        student_form = StudentForm(request.POST,instance=student)
        character_form = CharacterForm(initial={'character_name':request.POST.get('character_name')})
        if student_form.is_valid():
            student = student_form.save()
            student.character_set.update(name=request.POST.get('character_name'))
            return redirect('home')
        else:
            print(">>>>>student_form",student_form.errors)
        return render(request, 'student_form.html', {'student_form': student_form,
                                                     'character_form': character_form,
                                                     'header_name': "Update Student"})

class StudentDelete(RedirectView): # generally use for the redirecting to given url
    url = '/'

    # here below method is being customized to delete a student before redirect to given url
    def get_redirect_url(self,*args,**kwargs):
        pk = kwargs.get('pk')
        Student.objects.filter(id=pk).delete()
        return super().get_redirect_url(*args,**kwargs)


class StudentList(ListView):
    model = Student  # shows which model to use
    template_name = 'generic_views/student_list.html' # custom template name -> default appname/modelname_list.html
    context_object_name = 'students'  # custom object name -> default model_list here student_list
    ordering = ['date_of_birth']


    def get_queryset(self):  # to customize queryset -> default all()
        return Student.objects.filter(character__name__icontains ='vampire')

    def get_context_data(self): # custom or extra passing data
        context = super().get_context_data()
        context['humans'] = Student.objects.filter(~Q(character__name__icontains ='vampire'))
        return context

