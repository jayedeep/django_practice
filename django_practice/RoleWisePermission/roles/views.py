from django.shortcuts import render,redirect
from .forms import RegisterForm,RolesForm,LoginForm,FacultyForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Roles

# Create your views here.
def home(request):
    return render(request,'roles/home.html')


def register(request):
    user_form = RegisterForm()
    role_form = RolesForm()
    if request.method == 'POST':
        user_form = RegisterForm(request.POST or None)
        role_form = RolesForm(request.POST or None)
        if user_form.is_valid() or role_form.is_valid():
            user = user_form.save()
            role = role_form.save(commit=False)
            role.user_id = user.id
            role.save()
            messages.success(request,'Registration successful')
            messages.success(request,'Role created successfully')
            return redirect('login')
        else:
            messages.warning(request,'Registration failed! please try again')
    return render(request, 'roles/register.html',{'user_form':user_form,'role_form':role_form})

def login_fun(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                print(form.errors)
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Something went wrong')
    return render(request, 'roles/login.html',{'form':form})


def logout_fun(request):
    logout(request)
    return redirect('/')

def add_faculty(request,role='teacher'):
    user_form = FacultyForm()
    if request.method == 'POST':
        user_form = FacultyForm(request.POST or None)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password('laptop123')
            user.save()
            Roles.objects.create(role_name = role,user = user)
            ##### Add Group from here
            user.groups.create
            messages.success(request, f'{role} created successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Creation failed! please try again')
    return render(request, 'roles/register.html', {'user_form': user_form})

