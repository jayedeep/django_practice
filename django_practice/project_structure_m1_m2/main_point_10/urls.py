from django.urls import path
from .views import index2


urlpatterns = [
    path('index2',index2,name='use_of_base_template')
]