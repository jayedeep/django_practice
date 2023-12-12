from django.urls import path
from .views import list_permissions

urlpatterns =[
    path('permissions',list_permissions,name='list_permissions')
]