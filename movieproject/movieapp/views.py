from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm
# Create your views here.
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)

    return render(request,'detail.html',{'movie':movie})
def movie(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'movie.html',context)
def addm(request):
    if request.method=="POST":
        name=request.POST.get('name')
        descr = request.POST.get('descr')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=name,descr=descr,year=year,img=img)
        movie.save()

    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})
def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return  redirect('/')
    return render(request,'delete.html')
