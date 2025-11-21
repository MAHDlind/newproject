from django.urls import path
from .views import home

app_name = 'HomePage'

urlpatterns = [
    path('', home, name='WFpage'),
]