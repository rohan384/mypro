from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Bustime
# from .models import Busroute
from .form import TimeTable
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .form import route

# Create your views here.
def index(request):
	t_form=TimeTable()
	return render(request,"driver/admin.html",{'form':t_form})

def addbus(request):
    try:
        if request.method=="POST":
            t_form=TimeTable(request.POST)
            if t_form.is_valid():
                t_form.save()
        return render(request,'driver/admin.html',{'form':t_form,"msg":"BusTime added"})
    
    except Exception as error:
        print(error)
        return HttpResponse("Error")

def table(request):
    obj=Bustime.objects.all()
    return render(request,'driver/table.html',{'data':obj})

def update(request,pk):
    obj=Bustime.objects.get(id=pk)
    if request.method=='POST':
        obj=Bustime.objects.get(id=pk)
        obj.bus_name=request.POST.get('bus_name')
        obj.b_from=request.POST.get('b_from')
        obj.departure=request.POST.get('departure')
        obj.to=request.POST.get('to')
        obj.arrival=request.POST.get('arrival')
        obj.stops=request.POST.get('stops')
        obj.save()
        return redirect('view')  
    return render(request,'driver/update.html',{'data':obj})

def delete(request,pk):
    obj=Bustime.objects.get(id=pk)
    obj.delete()
    return table(request)

# def stops(request):
#     routeform=route()
#     return render(request,"driver/admin1.html",{'form':routeform})

# def addstop(request):
#     try:
#         if request.method=="POST":
#             routeform=route(request.POST)
#             if routeform.is_valid():
#                 routeform.save()
#         return render(request,'driver/admin1.html',{'form':routeform,"msg":"Stop added"})
#     except Exception as error:
#         print(error)
#         return HttpResponse("Error")
    
# def stopview(request):
#     obj=Busroute.objects.all()
#     return render(request,'driver/stops.html',{'data':obj})

def app(request):
    return render(request,'BusTime.html')

@login_required
def home(request):
	return render(request,'driver/admin.html')

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"registration/login.html")
        
def logout_view(request):
    logout(request)
    return redirect('login')


def sign_up(request):
        uform = UserCreationForm(request.POST)
        if request.method == "POST":
            if uform.is_valid():
                uname = uform.cleaned_data.get('username')
                pwd = uform.cleaned_data.get('password1')
                email=uform.cleaned_data.get('email')
                user1=User.objects.create_user(username=uname,password=pwd,email=email)
                user1.save()
                user = authenticate(request, username=uname, password=pwd)
                login(request,user)
                return redirect('home')
        else:
            uform = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': uform})
    
def Resethome(request):
    return render(request,'registration/ResetPassword.html')

def resetPassword(request):
    responseDic={}
    try:
        usern = request.POST['uname']
        recepient=request.POST['email']
        pwd=request.POST['password']
        #subject="Password reset"
        try:
            user=User.objects.get(username=usern)
            if user is not None:
                user.set_password(pwd)
                user.save()
                #send_mail(subject,message, EMAIL_HOST_USER, [recepient])
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exist"
            return render(request,"registration/ResetPassword.html",responseDic)
        
    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)


def index2(request):
    return render(request,'driver/index.html')
