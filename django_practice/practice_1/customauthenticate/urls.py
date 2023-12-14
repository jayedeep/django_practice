from django.urls import path
from .views import home,register,login_fun,logout_fun,profiledetail,get_verify

urlpatterns = [
    path('',home,name='home'),
    path('register',register,name='register'),
    path('login',login_fun,name='login'),
    path('logout',logout_fun,name='logout'),
    path('profiledetail',profiledetail,name='profiledetail'),
    path('get_verify',get_verify,name='get_verify'),

]