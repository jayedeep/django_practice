from django.shortcuts import render,redirect
from django.template.context_processors import request

from .forms import TaskFormset,TaskModelFormset,AuthorForm,BookFormSet
from .models import Task, Author


def create_tasks(request):
    print('...formset Task...')

    if request.method == 'POST':
        formset = TaskFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                task = Task.objects.create(name=form.cleaned_data['name'],description=form.cleaned_data['description'])
                task.save()
                print('........task has been saved!!!!!')
            # process the formset data
        else:
            print('form is not valid',formset.errors)
    formset = TaskFormset()
    return render(request, 'create_tasks.html', {'formset': formset})

def create_model_task(request):
    print('...Model Formset Task...')
    if request.method == 'POST':
        formset = TaskModelFormset(request.POST,queryset=Task.objects.none())
        if formset.is_valid():
            for form in formset:
                form.save()
                print('........task has been saved!!!!!')
            # process the formset data
        else:
            print('form is not valid',formset.errors)
    formset = TaskFormset()
    return render(request, 'create_tasks.html', {'formset': formset})


def create_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        book_formset = BookFormSet(request.POST)

        if author_form.is_valid() and book_formset.is_valid():
            author = author_form.save()
            books = book_formset.save(commit=False)
            for book in books:
                book.author = author
                book.save()
            return redirect('author_list')
    else:
        author_form = AuthorForm()
        book_formset = BookFormSet()

    context = {
        'author_form': author_form,
        'book_formset': book_formset,
    }
    return render(request, 'create_author.html', context)

def author_list(request):
    return render(request,'author_list.html',{'authors':Author.objects.all()})

def create_tasks_formsets(request):
    print('...formset dynamic Task...')

    if request.method == 'POST':
        formset = TaskFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                print(".>>>>>>form",form.cleaned_data)
                if form.cleaned_data.get('DELETE',None) and not form.cleaned_data.get('DELETE'):
                    task = Task.objects.create(name=form.cleaned_data['name'],description=form.cleaned_data['description'])
                    task.save()
                    print('........task has been saved!!!!!')
            # process the formset data
        else:
            print('form is not valid',formset.errors)
    formset = TaskFormset()
    return render(request, 'create_tasks_dynamic_formset.html', {'formset': formset})


