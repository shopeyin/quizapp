from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from account.models import MyUser,Student,Subject
from . forms import StudentSignUpForm
from django.views.generic import CreateView



# class StudentSignUpView(CreateView):
#     model = MyUser
#     form_class = StudentSignUpForm
#     template_name =  'student/student_register.html'


#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('home')
# Create your views here.


# def student_register(request):
#     context = {}
#     if request.method == "POST":
#         form=StudentSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
    
#     return render(request, 'student/student_register.html',context) 


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
    return render(request, 'student/student_profile.html',context) 