from django.shortcuts import render
from .models import Meter

def home(request):
    return render(request, 'microtec/home.html')

def leaktesting(request):
    return render(request, 'microtec/leaktesting.html')

def calibrations(request):
    return render(request, 'microtec/calibrations.html')

def repairs(request):
    return render(request, 'microtec/repairs.html')

def newinstruments(request):
    meters = Meter.objects.all()
    return render(request, 'microtec/newinstruments.html', {'meters':meters})

def forms(request):
    return render(request, 'microtec/forms.html')
