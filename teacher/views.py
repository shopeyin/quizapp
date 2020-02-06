from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from account.models import MyUser,Student,Subject,Teacher
from .forms import TeacherSignUpForm,SubjectForm


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



# def teacher_profile(request):
#     context={}
#     if request.method == 'POST':
#         subject = Subject(teacher=request.user)
#         print(subject)
#         form = SubjectForm(request.POST,instance=subject)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher:profile')
#     else:
#         form = SubjectForm()
#     context={'form':form}
#     subject_taught = Subject.objects.filter(teacher__user=request.user)
#     context['subject_taught'] = subject_taught
#     return render(request, 'teacher/teacher_profile.html',context) 




def teacher_profile(request):
    context={}
    if request.method == 'POST':
        user=Teacher.objects.get(user=request.user)
        subject = Subject(teacher=user)
        form = SubjectForm(request.POST, instance=subject)
        form.save()
        return redirect('teacher:profile')
    else:
        form = SubjectForm()
    context={'form':form}
    subject_taught = Subject.objects.filter(teacher__user=request.user)
    context['subject_taught'] = subject_taught
    return render(request, 'teacher/teacher_profile.html',context) 



    
    