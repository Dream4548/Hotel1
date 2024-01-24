from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render('index.html')

def about(request):
    return render('about.html')

def contact(request):
    return render('contact.html')