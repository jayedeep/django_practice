from django.shortcuts import render,redirect
from .forms import CustomAuthenticationForm,RegisterForm,ProfileForm,CodeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
# Create your views here.

@login_required(login_url='/login')
def home(request):
    return render(request,'customauthenticate/home.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("Registered successfully")
            return redirect('login')
        else:
            print("Failed to register")
    return render(request, 'customauthenticate/register.html',{'form':form})

def login_fun(request):
    form = CustomAuthenticationForm()
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request,data=request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                request.session['pk'] = user.id
                code = user.code_set.first()
                code.code = '123456'
                code.save()
                ### send email from here
                print("email sent with 123456")
                # login(request=request, user=user)
                print("Please Check Your email")
                return redirect('get_verify')
            else:
                print("got some error")
        else:
            print("Failed to login")
    return render(request, 'customauthenticate/login.html',{'form':form})

def get_verify(request):
    form = CodeForm()
    if request.method == 'POST':
        pk = request.session['pk']
        user = CustomUser.objects.get(pk=pk)
        code = user.code_set.first()
        form = CodeForm(request.POST,instance=code)
        if form.is_valid():
            form.save()
            login(request=request, user=user)
            print("login successful")
            return redirect('/')
        else:
            print("Got something wrong")
    return render(request, 'customauthenticate/verify.html',{'form':form})

def logout_fun(request):
    logout(request)
    return redirect('/')

@login_required
def profiledetail(request):
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            print(">>> profile updated")
            return redirect('/')
        else:
            print(">>> got something wrong")
    return render(request, 'customauthenticate/profiledetail.html',{'form':form})

