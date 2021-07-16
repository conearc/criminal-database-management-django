from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse


def CriminalEntryView(request):
    if request.method == 'POST':
        f = CriminalForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = CriminalForm()
    if request.user.is_staff:
        return render(request, 'criminal.html', {'form': f})
    return render(request, 'criminal1.html', {'form': f})

# Criminal Detail Entry View


def CriminalView(request):
    context = {'criminals': None}
    try:
        name = request.GET['name']
        print(name)
        criminals = Criminal.objects.filter(name__icontains=name)
        print(criminals)
        context['criminals'] = criminals
        if request.user.is_staff:
            return render(request, 'criminalhome.html', context)
        return render(request, 'criminalhome1.html', context)
    except:
        print("No search name provided")
    if request.user.is_staff:
        return render(request, 'criminalhome.html', context)
    return render(request, 'criminalhome1.html', context)


def handle_uploaded_file(f):
    with open('criminal/searchimages/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def SearchCriminal(request):
    if request.method == 'POST':
        f = SearchCriminalForm(request.POST, request.FILES)
        if f.is_valid():
            criminals = Criminal.objects.all()
            context = {'criminals': None}
            matchedcriminals = []
            for criminal in criminals:
                if criminal.image != '':
                    import face_recognition
                    known_image = face_recognition.load_image_file(
                        str(criminal.image))
                    handle_uploaded_file(request.FILES["image"])
                    filename = "criminal/searchimages/" + \
                        str(f.cleaned_data["image"])
                    print(filename)
                    unknown_image = face_recognition.load_image_file(filename)
                    try:
                        biden_encoding = face_recognition.face_encodings(known_image)[
                            0]
                        unknown_encoding = face_recognition.face_encodings(unknown_image)[
                            0]
                        results = face_recognition.compare_faces(
                            [biden_encoding], unknown_encoding)
                        print(results)
                        if str(results[0]) == "True":
                            print("correct")
                            matchedcriminals.append(criminal)
                    except:
                        print("no face")
            context['criminals'] = matchedcriminals
            print(matchedcriminals)
            if request.user.is_staff:
                return render(request, 'criminalsearch.html', context)
            return render(request, 'criminalsearch1.html', context)
    else:
        f = SearchCriminalForm()
    if request.user.is_staff:
        return render(request, 'searchcriminal.html', {'form': f})
    return render(request, 'searchcriminal1.html', {'form': f})


def CriminalUpdateView(request, id):
    criminal = Criminal.objects.all().get(id=id)
    if request.method == 'POST':
        f = CriminalForm(request.POST, instance=criminal)
        if f.is_valid():
            instance = f.save()
            return redirect('home')

    else:
        f = CriminalForm(instance=criminal)
    if request.user.is_staff:
        return render(request, 'criminalupdate.html', {'form': f})
    return redirect("home")


def DeleteCriminal(request, id):
    criminal = Criminal.objects.all().get(id=id)
    criminal.delete()
    print(criminal)
    return HttpResponse(200)
