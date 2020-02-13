from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from account.models import MyUser,Student,Subject,Quiz
from . forms import StudentSignUpForm,AnswerForm
from django.views.generic import CreateView


def student_register(request):
    if request.method == 'POST':
        form=StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect('student:profile')
    else:
        form = StudentSignUpForm()
    return render(request, 'student/student_register.html',{'form': form}) 



def student_profile(request):
    context={}
    student = Student.objects.filter(user=request.user).first() 
    student_subjects = student.subject.all()  
    context['student_subjects'] = student_subjects
    return render(request, 'student/student_profile.html',context) 



def view_student_subject_quiz(request,slug):
    context ={}
    single_subject = get_object_or_404(Subject,slug=slug)
    print(single_subject)
    quiz = Quiz.objects.filter(subject__name=single_subject)
    context['single_subject'] = single_subject

    context['quiz'] = quiz
    return render(request, 'student/view_student_subject_quiz.html',context) 


def answer_quiz(request,slug):
    context = {}
    student = Student.objects.filter(user=request.user).first() 
    student_subjects = student.subject.all()  
    quiz = get_object_or_404(Quiz,slug=slug)
    convert_quiz= str(quiz.answer.lower()) 
    if request.method == 'POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer =  form.cleaned_data.get('answer')
            if answer.lower() == convert_quiz:
                messages.success(request, 'You are correct!')
            else:
                messages.warning(request, 'You are wrong,try again!')
    else:
        form = AnswerForm()
    context['form']=form
    context['quiz'] = quiz
    context['student_subjects'] = student_subjects
    return render(request, 'student/answer_quiz.html',context) 