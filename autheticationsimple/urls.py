from django.urls import path
from .views import register,login_fun,logout_fun

urlpatterns = [
    path('register',register,name='register'),
    path('login', login_fun, name='login'),
    path('logout', logout_fun, name='logout'),

]