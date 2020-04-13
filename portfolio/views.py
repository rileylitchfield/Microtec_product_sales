from django.shortcuts import render
from .models import Meter

def home(request):
    return render(request, 'portfolio/home.html')

def leaktesting(request):
    return render(request, 'portfolio/leaktesting.html')

def calibrations(request):
    return render(request, 'portfolio/calibrations.html')

def repairs(request):
    return render(request, 'portfolio/repairs.html')

def newinstruments(request):
    meters = Meter.objects.all()
    return render(request, 'portfolio/newinstruments.html', {'meters':meters})

def forms(request):
    return render(request, 'portfolio/forms.html')
