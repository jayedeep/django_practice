from django.urls import path
from .views import home,single_student,single_student_update,student_delete


urlpatterns = [
    path('',home,name='home'),
    path('<int:id>',single_student,name='single_student'),
    path('student/update/<int:id>',single_student_update,name='single_student_update'),
    path('student/delete/<int:id>',student_delete,name='student_delete')
]