from django.urls import path
from .views import (
   student_register,
   student_profile,
# StudentSignUpView
)

app_name = 'student'


urlpatterns= [
    path('',student_register,name='register'),
    path('profile/',student_profile,name='profile'),
    # path('',StudentSignUpView.as_view(),name='register'),
   
]