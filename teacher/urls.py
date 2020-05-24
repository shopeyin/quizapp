from django.urls import path
from .views import (
   teacher_register,
   teacher_profile,
   view_subject_quiz,
   delete_quiz_view,
   delete_subject_view
  
)

app_name = 'teacher'


urlpatterns= [
    path('',teacher_register,name='register'),
    path('profile/',teacher_profile,name='profile'),
    path('delete/<slug>',delete_quiz_view,name='delete'),
    path('deletes/<slug>',delete_subject_view,name='deletes'),
    path('view_quiz/<slug>/',view_subject_quiz,name='view_quiz')
]

