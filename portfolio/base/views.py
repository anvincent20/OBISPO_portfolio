from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms  import *

def home(request):
    user = User.objects.get(username='admin2')
    context = {'user_data':user}
    return render(request, 'home.html',context = context)


@login_required(login_url="/auth/login/")
def cms(request):
    user = request.user
    print(user)
    context = {'user_data':user}
    return render(request, 'cms.html',context=context)
    
#Into Form
@login_required(login_url="/auth/login/")
def personalprofile(request):
    user = request.user
    if request.method == 'POST':
        form = PeronalInfoForm(request.POST, request.FILES)
        if form.is_valid():

            try:
                cleaned_data = form.cleaned_data
                for field, value in cleaned_data.items():
                    if value: 
                        setattr(user, field, value)
                user.save()
                return redirect('base:cms')
            except Exception as e:
                print(f"Error:{e}")
        else:
                print(form.errors)
    else:
            form = PeronalInfoForm()

    return redirect('base:cms')

#About Me Form
@login_required(login_url="/auth/login/")
def aboutme(request):
    user = request.user
    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                cleaned_data = form.cleaned_data
                for field, value in cleaned_data.items():
                    if value: 
                        setattr(user, field, value)
                user.save()
                return redirect('base:cms')
            except Exception as e:
                print(f"Error:{e}")
        else:
                print(form.errors)
    else:
            form = AboutMeForm()

    return render(request, 'cms.html')


#Social Media Form
@login_required(login_url="/auth/login/")
def socialmedia(request):
    user = request.user
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                cleaned_data = form.cleaned_data
                for field, value in cleaned_data.items():
                    if value: 
                        setattr(user, field, value)
                user.save()
                return redirect('base:cms')
            except Exception as e:
                print(f"Error:{e}")
        else:
                print(form.errors)
    else:
            form = SocialMediaForm()

    return render(request, 'cms.html')


                        #PROJECT FORM
#CREATE PROJECT
@login_required(login_url="/auth/login/")
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

# UPDATE PROJECT
@login_required(login_url="/auth/login/")
def updateproject(request):
    if request.method == "POST":
        user = request.user
        try:
            project = Project.objects.get(user = user, id=request.POST.get('project_id'))

            for field, value in request.POST.items():
                if value: 
                    setattr(project, field, value)
            project.save()
            return redirect('base:cms')
        except Exception as e:
            print(e)
            return redirect('base:cms')

# DELETE PROJECT
@login_required(login_url="/auth/login/")
def deleteproject(request):

    if request.method == "POST":
        user = request.user
        try:
            project = Project.objects.get(user = user, id=request.POST.get('project_id'))
            project.delete()
            return redirect('base:cms')
        except Exception as e:
            print(e)
            return redirect('base:cms')