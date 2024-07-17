from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('api/studentsList/', StudenList.as_view(), name='students-list'),
    path('api/students/<int:id>/', StudentDetail.as_view(), name='students-detail'),
]