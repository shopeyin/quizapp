from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.contrib import messages
from account.models import MyUser,Student,Subject,Teacher,Quiz
from .forms import TeacherSignUpForm,AddquizForm,SubjectForm


def teacher_register(request):
    context = {}
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
    context['form'] = form
    return render(request, 'teacher/teacher_register.html',context) 






def teacher_profile(request):
    context={}
    if request.user.is_authenticated:
        if request.method == 'POST':
            user=Teacher.objects.get(user=request.user)
            subject = Subject(teacher=user)
            form = SubjectForm(request.POST, instance=subject)
            if form.is_valid():
                form.save()
                return redirect('teacher:profile')
        else:
            form = SubjectForm()
        context={'form':form}
        subject_taught = Subject.objects.filter(teacher__user=request.user)
        context['subject_taught'] = subject_taught
    else:
        return redirect('login')
    return render(request, 'teacher/teacher_profile.html',context) 



def view_subject_quiz(request,slug):
    context ={}
    user = request.user
    if request.user.is_authenticated:
        single_subject = get_object_or_404(Subject,slug=slug)

        if single_subject.teacher.user != user:
            return HttpResponse('You are not the owner of this subject or quiz ')

        context['single_subject'] = single_subject
        print(single_subject)

        quiz = Quiz.objects.filter(subject__name=single_subject)
       
        if request.method =='POST':
            create_quiz=Quiz(subject=single_subject)
            form=AddquizForm(request.POST,instance=create_quiz)
            if form.is_valid():
                form.save()
                return redirect('teacher:view_quiz',slug=slug)
        else:
            form = AddquizForm()
        context={'form':form} 

        
        context['quiz'] = quiz
    else:
        return redirect('login')
    single_subject = get_object_or_404(Subject,slug=slug)
    context['single_subject'] = single_subject
    return render(request, 'teacher/view_subject_quiz.html',context) 




def delete_quiz_view(request,slug): 
    quiz = get_object_or_404(Quiz,slug=slug)
    quiz.delete()
    messages.success(request,f"{quiz} quiz successfully deleted")
    return redirect('teacher:profile')


def delete_subject_view(request,slug): 
    subject = get_object_or_404(Subject,slug=slug)
    subject.delete()
    messages.success(request,f"{subject} subject successfully deleted")
    return redirect('teacher:profile')



    



    
    
