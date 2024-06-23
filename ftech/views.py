from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
import datetime
from django.shortcuts import redirect

from ftech.models import bookDemo

# Create your views here.
def render_index(request):
    return render(request,"index.html")

def register_page(request):
    return render(request,'registration_page.html')
# Create your views here.
def render_login(request):
    return render(request,"home/dashboard.html")

def perform_registration(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
       
        user_obj=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        user_obj.save()
        return render(request,"index.html")
    else:
        return HttpResponse('Registration failed.')

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    
    return redirect('/')


def perform_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        user_obj = authenticate(request,username=username,password=password)
        if user_obj is not None:
            login(request,user_obj)
            # questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
            return render(request,'dashboard_page.html')
        else:
            return HttpResponseRedirect('/')
    else :
        # questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
        return render(request,'dashboard_page.html')

def perform_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        user_obj = authenticate(request,username=username,password=password)
        if user_obj is not None:
            login(request,user_obj)
            # questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
            return render(request,'dashboard_page.html',{'questions':'questions_list'})
        else:
            return HttpResponseRedirect('/')
    else :
        # questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
        return render(request,'dashboard_page.html',{'questions':'questions_list'})


def perform_registration(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
       
        user_obj=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        user_obj.save()
        return render(request,"login.html")
    else:
        return HttpResponse('Registration failed.')
    
def submit_form(request):
    if request.method =='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        demo_obj=bookDemo.objects.create(name=name,phone=phone,email=email,subject=subject,message=message)
        demo_obj.save()
        return HttpResponse('true')
    else:
        return HttpResponse('false')