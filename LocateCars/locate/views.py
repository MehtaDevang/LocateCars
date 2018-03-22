from django.shortcuts import render
from .models import Vehicle, Journey
# Create your views here.
def home(request):
    vehicle = Vehicle.objects.all()
    journey = Journey.objects.all()
    context = {
        'vehicle' : vehicle,
        'journey' : journey,
    }
    return render(request, 'home.html', context)