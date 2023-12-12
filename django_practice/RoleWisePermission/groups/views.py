from django.shortcuts import render,redirect
from .forms import GroupForm,UpdateGroupForm
from django.contrib import messages
from .models import CustomGroup

# Create your views here.
def create_group(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Group created successfully")
            return redirect('group_list')
        else:
            messages.error(request,"Group creation failed")
    return render(request,'groups/create.html',{'form':form})

def group_list(request):
    groups = CustomGroup.objects.all()
    return render(request,'groups/list.html',{'groups':groups})

def update_group(request,id):
    group = CustomGroup.objects.get(id=id)
    form = UpdateGroupForm(instance=group)
    if request.method == 'POST':
        form = UpdateGroupForm(request.POST,instance=group)
        if form.is_valid():
            form.save()
            messages.success(request,"Group Update successfully")
            return redirect('group_list')
        else:
            messages.error(request,"Group Update failed")
    return render(request,'groups/create.html',{'form':form})

def delete_group(request,id):
    group = CustomGroup.objects.filter(id=id)
    group.delete()
    return redirect('group_list')