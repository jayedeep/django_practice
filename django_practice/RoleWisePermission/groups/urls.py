from django.urls import path
from .views import create_group,group_list,update_group,delete_group

urlpatterns = [
    path('groups/add',create_group,name='create_group'),
    path('groups',group_list,name='group_list'),
    path('groups/update/<int:id>', update_group, name='update_group'),
    path('groups/delete/<int:id>', delete_group, name='delete_group'),

]