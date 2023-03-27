from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_predict, name = 'input_predict')
]
