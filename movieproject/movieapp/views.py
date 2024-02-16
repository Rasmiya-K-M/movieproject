from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieform
# Create your views here.
#show in homepage
def index(request):
    mv=movie.objects.all()
    context={
        'key1':mv
    }
    # return HttpResponse("Hello movieapp",context)
    return render(request,'index.html',context)

#show seperatley by id
def detail(requet,movie_id):
    # return HttpResponse("This movie %s" % movie_id)
    mv2=movie.objects.get(id=movie_id)
    return render(requet,'detail.html',{'key2':mv2})

#add to adminpannel from form
def addMovie(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        desc2= request.POST.get('desc')
        year2= request.POST.get('year')
        img2= request.FILES['img']
        mv=movie(name=name1,desc=desc2,year=year2,img=img2)
        mv.save()
    return render(request,'add.html')

#update function
def updateMovie(request,id):
    mv3=movie.objects.get(id=id)
    fm=movieform(request.POST or None,request.FILES,instance=mv3)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    return render(request,'edit.html',{'fm':fm,'mv3':mv3})

def deleteMovie(request,id):
    if request.method== 'POST':
        mv4=movie.objects.get(id=id)
        mv4.delete()
        return redirect('/')
    return render(request,'delete.html')
