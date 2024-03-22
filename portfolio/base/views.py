from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms  import *

def home(request):
    user = User.objects.get(id=1)
    context = {'user_data':user}
    return render(request, 'home.html',context = context)

def cms(request):
    return render(request, 'cms.html')
    
#Into Form
@login_required
def personalprofile(request):
    user = request.user
    if request.method == 'POST':
        form = PeronalInfoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            try:
                form.save() 
                return redirect('base:cms')
            except Exception as e:
                print(f"Error:{e}")
        else:
                print(form.errors)
    else:
            form = PeronalInfoForm()

    return redirect('base:cms')

#About Me Form
@login_required
def aboutme(request):
    user = request.user
    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            try:
                form.save() 
                return redirect('base:cms')
            except Exception as e:
                print(f"Error:{e}")
        else:
                print(form.errors)
    else:
            form = AboutMeForm()

    return render(request, 'cms.html')

#Project Form
@login_required
def project(request):
    user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                instance = form.save(commit=False) 
                instance.user = user
                instance.save()

                print(instance)
                return redirect('base:cms')
            except Exception as e:
                print(f"Error:{e}")
        else:
                print(form.errors)
    else:
            form = ProjectForm()

    return render(request, 'cms.html')

#Social Media Form
@login_required
def socialmedia(request):
    user = request.user
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            try:
                form.save() 
                return redirect('base:cms')
            except Exception as e:
                print(f"Error:{e}")
        else:
                print(form.errors)
    else:
            form = SocialMediaForm()

    return render(request, 'cms.html')
