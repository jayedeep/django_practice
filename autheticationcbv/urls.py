from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import RegisterView
from .forms import LoginForm


urlpatterns = [
    path('',TemplateView.as_view(template_name = 'home.html'),name='home'),
    path('register',RegisterView.as_view(),name='register'),
    path('login',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm,success_url=''),name='login'),
    path('login',auth_views.LogoutView.as_view(),name='logout'),

]