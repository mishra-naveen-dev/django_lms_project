from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages

def REGISTER(request):

    # print(f"The request type is : {request.method}")
    email = None
    password = None
    username = None
    if request.method == "POST":
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')
       print(username,email,password)
       #    check username
       if User.objects.filter(email=email).exists():
           messages.warning(request,'Email are Already Exists !')
           return redirect('register')

       # check username
       if User.objects.filter(username=username).exists():
           messages.warning(request,'Username are Already exists !')
           return redirect('register')

       user = User (
          username=username,
          email=email,
        )
       user.set_password(password)
       user.save()
       return redirect('login')
    return render(request,'registration/register.html')

def Do_LOGIN(request):

    return None