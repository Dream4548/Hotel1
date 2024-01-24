from django.shortcuts import render,HttpResponse
from .forms import BookingForm 

# Create your views here.
def index(request):
    return render (request,'index.html')

def room(request):
    return render(request,'room.html')

def contact(request):
    return render(request,'contact.html')

def fa(request):
    return render(request,'fa.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})