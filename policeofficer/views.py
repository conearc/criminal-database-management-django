from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.shortcuts import render, redirect


# PoliceOfficer Detail Entry View

def PoliceOfficerEntryView(request):
    if request.method == 'POST':
        f = PoliceOfficerForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = PoliceOfficerForm()
    if request.user.is_staff:
        return render(request, 'policeofficer.html', {'form': f})
    return redirect("home")


def PoliceOfficerUpdateView(request, id):
    policeofficer = PoliceOfficer.objects.all().get(id=id)
    if request.method == 'POST':
        f = PoliceOfficerForm(request.POST, instance=policeofficer)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = PoliceOfficerForm(instance=policeofficer)
    if request.user.is_staff:
        return render(request, 'policeofficerupdate.html', {'form': f})
    return redirect("home")


def PoliceOfficerHomeView(request):
    context = {'policeofficers': None}
    try:
        name = request.GET['name']
        print(name)
        policeofficers = PoliceOfficer.objects.filter(name__icontains=name)
        print(policeofficers)
        context['policeofficers'] = policeofficers
        if request.user.is_staff:
            return render(request, 'policeofficerhome.html', context)
        return render(request, 'policeofficerhome1.html', context)
    except:
        print("No search name provided")
    if request.user.is_staff:
        return render(request, 'policeofficerhome.html', context)
    return render(request, 'policeofficerhome1.html', context)
