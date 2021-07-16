from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.shortcuts import render, redirect


# PoliceStaion Detail Entry View


def PoliceStationEntryView(request):
    if request.method == 'POST':
        f = PoliceStationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = PoliceStationForm()
    if request.user.is_staff:
        return render(request, 'policestation.html', {'form': f})
    return redirect("home")


def PoliceStationUpdateView(request, id):
    policestation = PoliceStation.objects.all().get(id=id)
    if request.method == 'POST':
        f = PoliceStationForm(request.POST, instance=policestation)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = PoliceStationForm(instance=policestation)
    if request.user.is_staff:
        return render(request, 'policestationupdate.html', {'form': f})
    return redirect("home")


def PoliceStationHomeView(request):
    context = {'policestations': None}
    try:
        name = request.GET['name']
        print(name)
        policestations = PoliceStation.objects.filter(name__icontains=name)
        print(policestations)
        context['policestations'] = policestations
        if request.user.is_staff:
            return render(request, 'policestationhome.html', context)
        return render(request, 'policestationhome1.html', context)
    except:
        print("No search name provided")
    if request.user.is_staff:
        return render(request, 'policestationhome.html', context)
    return render(request, 'policestationhome1.html', context)
