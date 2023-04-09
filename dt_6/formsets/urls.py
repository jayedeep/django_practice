from django.urls import path
from .views import create_tasks,create_model_task,author_list,create_author,create_tasks_formsets

urlpatterns =[
    path('',create_tasks,name='create_tasks'),
    path('create/model/task', create_model_task, name='create_model_task'),
    path('list/author',author_list,name='author_list'),
    path('create/author',create_author,name='create_author'),

    path('create/tasks/formsets', create_tasks_formsets, name='create_tasks_formsets'),


]