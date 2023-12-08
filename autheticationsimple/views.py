from django.shortcuts import render,redirect
from .forms import SignupForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations!, you have signed up")
            return redirect('login')
        else:
            messages.error(request, "Something went wrong!")
    return render(request, 'autheticationsimple/register.html',{'form':form})

def login_fun(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                messages.success(request, "You have been successfully logged in")
                return redirect('/')
            else:
                messages.error(request, "Something went wrong!")
    return render(request, 'autheticationsimple/login.html',{'form':form})

def logout_fun(request):
    logout(request)
    messages.success(request, "You have been logout successfully")
    return redirect('/')
