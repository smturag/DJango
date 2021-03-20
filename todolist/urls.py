from django.urls import path
from todolist import views

urlpatterns = [
    path('name/', views.user, name='user'),
    path('forms/', views.userform, name='form')
]
