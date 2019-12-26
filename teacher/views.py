from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from account.models import MyUser,Student,Subject
from .forms import TeacherSignUpForm


def teacher_register(request):
    if request.method == 'POST':
        form=TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect('teacher:profile')
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher/teacher_register.html',{'form': form}) 



def teacher_profile(request):
    context={}
    return render(request, 'teacher/teacher_profile.html',context) 
