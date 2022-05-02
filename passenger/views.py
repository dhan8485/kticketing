from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'passenger/index.html')

def UserBooking(request):
    return render(request,'passenger/Booking.html')