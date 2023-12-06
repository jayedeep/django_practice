from django.urls import path
from .views import home,single_profile,single_profile_update,profile_delete,download_file


urlpatterns = [
    path('',home,name='home'),
    path('<int:id>',single_profile,name='single_profile'),
    path('profile/update/<int:id>',single_profile_update,name='single_profile_update'),
    path('profile/delete/<int:id>',profile_delete,name='profile_delete'),
    path('download/<int:id>/', download_file, name='download_file'),

]