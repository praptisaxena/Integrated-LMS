from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.EmailBackEnd import EmailBackEnd



def REGISTER(request):
    if request.method == "POST":
        print(request.POST)  # This will print all POST data to the console
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username, email, password)

        #check email
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email already exist!')
            return redirect('register')

        #check username
        if User.objects.filter(username=username).exists():
            messages.warning(request,'username already exists!')
            return redirect('register')

        user=User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')


    return render(request, 'registration/register.html')



def DO_LOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackEnd.authenticate(request,
                                         username=email,
                                         password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')
