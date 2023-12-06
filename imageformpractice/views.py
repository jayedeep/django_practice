from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from django.http import FileResponse


# Create your views here.
def home(request):
    form = ProfileForm()
    profiles = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile record inserted.")
            return redirect('home')
        else:
            messages.error(request, "Got error on Create new record.")
    return render(request, 'imageformpractice/home.html',{'profiles':profiles,'form':form})


def single_profile(request,id):
    profile = get_object_or_404(Profile,id=id)
    return render(request, 'imageformpractice/single_profile.html',{'profile':profile})

def single_profile_update(request,id):
    profile = get_object_or_404(Profile,id=id)
    profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST or None, request.FILES or None,instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile record updated.")
            return redirect('home')
        else:
            messages.error(request, "Got error on Update record.")
    return render(request, 'imageformpractice/single_profile_update.html',{'profile_form':profile_form})

def profile_delete(request,id):
    profiles = Profile.objects.filter(id=id)
    profiles.delete()
    messages.success(request, "Profile record deleted.")
    return redirect('home')

def download_file(request, id):
    my_profile = get_object_or_404(Profile, pk=id)
    response = FileResponse(my_profile.file, as_attachment=True)
    return response