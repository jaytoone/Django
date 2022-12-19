from django.urls import path
from . import views

app_name = 'attends'

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('result/', views.result, name='result'),
]
