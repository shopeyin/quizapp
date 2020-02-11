from django.urls import path
from .views import (
   student_register,
   student_profile,
   view_student_subject_quiz,
   answer_quiz,
)

app_name = 'student'


urlpatterns= [
    path('',student_register,name='register'),
    path('profile/',student_profile,name='profile'),
    path('view_quiz/<slug>',view_student_subject_quiz,name='view_quiz'),
    path('answer_quiz/<slug>',answer_quiz,name='answer_quiz'),
]