from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("base:cms"))
        else:
            print("cant login")
            
    return render(request, 'signin.html')

@login_required(login_url="/auth/login/")
def signout(request):
    logout(request)  
    return redirect(reverse("base:home"))

@login_required(login_url="/auth/login/")
def changepass(request):  

    if request.method == "POST":
        user = request.user
        password = request.POST.get("password", user.password)
        user.set_password()
        user.save()
    return redirect(reverse("base:cms"))
