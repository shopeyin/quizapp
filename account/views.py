from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from . forms import AccountAuthenticateForm




def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticateForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)
            if user and user.is_teacher:
                login(request, user)
                return redirect('teacher:profile')
            elif user and user.is_student:
                login(request,user)
                return redirect('student:profile')
            else:
                login(request,user)
                return redirect('home')
    else:
        form = AccountAuthenticateForm()

    context['form'] = form    
    return render(request, 'account/login.html',context) 

