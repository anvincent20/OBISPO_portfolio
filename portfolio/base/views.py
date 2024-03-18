from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

    
def cms(request):
    return render(request, 'cms.html')
    