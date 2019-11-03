from django.shortcuts import render, redirect
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservation_form = ReservationForm()
    context = {
        'reservation_form': reservation_form
    }
    return render(request, 'reservations/index.html', context)