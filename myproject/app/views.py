from django.shortcuts import render,redirect
from app.models import crud
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

@login_required(login_url='logs')
def text(request):
    if request.method=="POST":
        name=request.POST['name']
        email = request.POST['email']
        password=request.POST['password']
        print(name)
        
        data=crud.objects.create(name=name,email=email,password=password)
        data.save()
        return redirect('register')
        
    context={}
    return render(request,"admin/text.html",context)

@login_required(login_url='logs')
def get(request):
    data = crud.objects.all()
    context = {'mydata': data}
    return render(request,"admin/get.html",context)

@login_required(login_url='logs')  
def read(request,id):
    data = crud.objects.get(id=id)
    context = {'post': data}
    return render(request,"admin/read.html",context)

@login_required(login_url='logs')
def update(request,id):
    data = crud.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        email = request.POST['email']
        password=request.POST['password']
        
        data.name = name
        data.email = email
        data.password = password
        data.save()
        
        data=crud.objects.create(name=name,email=email,password=password)
        data.save()
        return redirect('get')
    context={'post':data}
    return render(request,"admin/update.html",context)

@login_required(login_url='logs')
def delete(request,id):
    data = crud.objects.get(id=id)
    data.delete()
    return redirect('get')


def register(request):
    if request.method == 'POST':
        u_name=request.POST['username']
        u_phone=request.POST['phone']
        u_email=request.POST['email']
        u_password=request.POST['password']
        c_password=request.POST['c_password']

        if u_password == c_password:
            data=User.objects.create_user(username=u_email,email=u_email,first_name=u_phone,password=u_password)
            data.save()
        else:
            return HttpResponse('Your password is miss match')
        
    context={}
    return render(request,'admin/register.html',context)



def logs(request):
    if request.method == 'POST':
        u_email=request.POST['email']
        u_password=request.POST['password']
        if not User.objects.filter(username=u_email).exists():
            
            messages.error(request, 'Invalid Username')
            return redirect('/logs')
        
        
        user = authenticate(username=u_email, password=u_password)
        
        if user is None:
            
            messages.error(request, "Invalid Password")
            return redirect('/logs')
        else:
            
            login(request, user)
            return redirect('/get')
    context={}
    return render(request,'admin/log.html',context)


def getuser(request):
    data = crud.objects.all()
    context = {'mydata': data}
    return render(request,"user/getuser.html",context)

 
def readuser(request,id):
    data = crud.objects.get(id=id)
    context = {'post': data}
    return render(request,"user/read1.html",context)