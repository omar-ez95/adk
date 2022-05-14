from django.shortcuts import render
from .models import * 
# Create your views here
from django.shortcuts import redirect

def index(request):
    washing = Washing.objects.filter(type= 2)
    dryer =  Washing.objects.filter(type= 1)
    context = {
        'washing':washing,
        'dryer': dryer
    }
    return render(request, 'index.html', context)


def turnWashing(request,id):
    washing = Washing.objects.get(id=id)
    if washing.on == True:
        washing.on = False
    else: 
        washing.on = True
    washing.save()
    return redirect('home')

def turndryer(request,id):
    dryer = Dry.objects.get(id=id)
    if dryer.on == True:
        dryer.on = False
    else: 
        dryer.on = True
    dryer.save()
    return redirect('home')

