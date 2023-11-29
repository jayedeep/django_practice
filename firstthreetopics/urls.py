from django.urls import path
from .views import HomePageView,StudentUpdate,StudentDelete,StudentList

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('update/<int:pk>', StudentUpdate.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),

#     generic cbv
    path('cbv',StudentList.as_view(), name='student_list'),
]