from django.shortcuts import render, redirect, get_object_or_404
from .models import StandUser, Stand

# Create your views here.

def home(request):
    return render(request, 'home.html')


# Stand Users

def list_standusers(request):
    standusers = StandUser.objects.all()
    return render(request, 'list_standuser.html', {"standusers": standusers})

def create_standuser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        nationality = request.POST.get("nationality")
        standuser = StandUser()
        standuser.name = name
        standuser.age = age
        standuser.nationality = nationality
        standuser.save()
        return redirect('list-standusers')
    return render(request, 'form_standuser.html')

def update_standuser(request, id):
    standuser = get_object_or_404(StandUser, pk=id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        nationality = request.POST.get("nationality")
        standuser.name = name
        standuser.age = age
        standuser.nationality = nationality
        standuser.save()
        return redirect('list-standusers')
    return render(request, 'form_standuser.html', {"standuser": standuser})

def delete_standuser(request, id):
    standuser = get_object_or_404(StandUser, pk=id)
    standuser.delete()
    return redirect('list-standusers')


# Stands

def list_stands(request):
    stands = Stand.objects.all()
    return render(request, 'list_stand.html', {"stands":stands})


def create_stand(request):
    standusers = StandUser.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        ability = request.POST.get("ability")
        user = request.POST.get("user")
        stand = Stand()
        stand.name = name
        stand.ability = ability
        stand.user = get_object_or_404(StandUser, pk=user)
        stand.save()
        return redirect('list-stands')
    return render(request, 'form_stand.html', {"standusers": standusers})

def update_stand(request, id):
    standusers = StandUser.objects.all()
    stand = get_object_or_404(Stand, pk=id)
    if request.method == "POST":
        name = request.POST.get("name")
        ability = request.POST.get("ability")
        user = request.POST.get("user")
        stand.name = name
        stand.ability = ability
        stand.user = get_object_or_404(StandUser, pk=user)
        stand.save()
        return redirect('list-stands')
    return render(request, 'form_stand.html', {"standusers": standusers, "stand": stand})

def delete_stand(request, id):
    stand = get_object_or_404(Stand, pk=id)
    stand.delete()
    return redirect('list-stands')
    