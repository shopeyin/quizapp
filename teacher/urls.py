from django.urls import path
from .views import (
   teacher_register,
   teacher_profile,
)

app_name = 'teacher'


urlpatterns= [
    path('',teacher_register,name='register'),
    path('profile/',teacher_profile,name='profile'),
]