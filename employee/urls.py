from django.urls import path
from employee.views import *

urlpatterns = [
    path('list/', employee_list, name='employee-list'),
]