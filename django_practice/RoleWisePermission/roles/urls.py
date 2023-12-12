from django.urls import path
from .views import register,login_fun,logout_fun,home,add_faculty

urlpatterns = [
    path('',home,name='home'),
    path('register', register,name='register'),
    path('login', login_fun,name='login'),
    path('logout', logout_fun,name='logout'),

    path('add_faculty',add_faculty,name='add_faculty'),
    path('add_faculty/<str:role>',add_faculty,name='add_student')
]
