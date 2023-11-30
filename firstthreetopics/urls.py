from django.urls import path
from .views import (HomePageView,StudentUpdate,StudentDelete,
                    StudentList,StudentDetail,StudentCreateForm,StudentCreate2Form)

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('update/<int:pk>', StudentUpdate.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),

#     generic cbv
    path('cbv',StudentList.as_view(), name='student_list'),
    path('cbv/detail/<int:id>', StudentDetail.as_view(), name='student_detail'),
    path('cbv/create/', StudentCreateForm.as_view(), name='student_create'),
    path('cbv/create2/', StudentCreate2Form.as_view(), name='student_create_second'),



]