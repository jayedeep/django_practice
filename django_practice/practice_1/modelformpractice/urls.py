from django.urls import path
from .views import home,single_teacher,single_teacher_update,teacher_delete


urlpatterns = [
    path('',home,name='home'),
    path('<int:id>',single_teacher,name='single_teacher'),
    path('teacher/update/<int:id>',single_teacher_update,name='single_teacher_update'),
    path('teacher/delete/<int:id>',teacher_delete,name='teacher_delete')
]