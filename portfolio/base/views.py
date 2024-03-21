from django.shortcuts import render
from .models import *
from .forms  import *

def home(request):
    return render(request, 'home.html')

    
def cms(request):
    return render(request, 'cms.html')
    
def personalprofile(request):
    user=User.objects.get(id = 1)
    if request.method == 'POST':
        form = PeronalInfoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            try:
                form.save()
                return redirect('base:personal_information')
            except Exception as e:
                print(f"Error:{e}")
                context = {'form': form, 'error_message': "There was a problem saving the skill. Please try again."}
        else:
                print(form.errors)
    else:
            form = PeronalInfoForm

    context = {'form': form, 'user':user}
    return render(request, 'cms.html', context)