from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout

def home_view(request):
    context = {}
    return render(request,'home/index.html',context)


def logout_view(request):
    logout(request)
    return redirect('home')