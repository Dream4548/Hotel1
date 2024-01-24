from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render (request,'index.html')

def room(request):
    return render(request,'room.html')

def contact(request):
    return render(request,'contact.html')

def fa(request):
    return render(request,'fa.html')