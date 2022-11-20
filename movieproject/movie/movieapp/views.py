from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Movieform

# Create your views here.
from .models import Movie


def index(request):
    movie = Movie.objects.all()
    context = {'Movies_list': movie}
    return render(request, 'index.html', context)


def detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "details.html", {'movie': movie})


def add(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        des = request.POST.get("Des")
        year = request.POST.get('Year')
        img = request.FILES['img']
        movie = Movie(Name=name, Des=des, Year=year, img=img)
        movie.save()
        return redirect('/')
    return render(request, "add.html")


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})
def delete(request,id):
    if request.method == "POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

