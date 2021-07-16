from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.shortcuts import render, redirect


# Crime Detail Entry View
@login_required("")
def CrimeEntryView(request):
    if request.method == 'POST':
        f = CrimeForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = CrimeForm()
    if request.user.is_staff:
        return render(request, 'crime.html', {'form': f})
    return render(request, 'crime1.html', {'form': f})


def CrimeView(request):
    context = {'stations': None}
    try:
        name = request.GET['name']
        print(name)
        policestations = PoliceStation.objects.filter(name__icontains=name)
        print(policestations)
        context['stations'] = policestations
        if request.user.is_staff:
            return render(request, 'crimehome.html', context)
        return render(request, 'crimehome1.html', context)
    except:
        print("No search name provided")
    if request.user.is_staff:
        return render(request, 'crimehome.html', context)
    return render(request, 'crimehome1.html', context)


def CrimeUpdateView(request, id):
    crime = Crime.objects.all().get(id=id)
    if request.method == 'POST':
        f = CrimeForm(request.POST, instance=crime)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = CrimeForm(instance=crime)
    if request.user.is_staff:
        return render(request, 'crimeupdate.html', {'form': f})
    return redirect("home")


def CrimeListView(request):
    context = {'crimes': None}
    try:
        id = request.GET['id']
        print(id)
        p = PoliceStation.objects.get(id=id)
        crimes = Crime.objects.filter(policestation=p)
        print(crimes)
        context['crimes'] = crimes
        if request.user.is_staff:
            return render(request, 'crimelist.html', context)
        return render(request, 'crimelist1.html', context)
    except:
        print("No search name provided")
    if request.user.is_staff:
        return render(request, 'crimelist.html', context)
    return render(request, 'crimelist1.html', context)
