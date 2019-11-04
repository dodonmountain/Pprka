from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Customer, Room, Reservation
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# 예약할때 비회원일시, 회원일시로 나눠서
def index(request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            # temp_user = User.objects.create(phone_number='', email='*****@*****.***')
            reservation = reservation_form.save(commit=False)
            reservation.customer = temp_user
            reservation.save()
            # 결제 페이지로 이동
            return redirect('') 
    else :
        temp_reservation_form = ReservationForm()
    context = {
        'temp_reservation_form': temp_reservation_form
    }
    return render(request, 'reservations/index.html', context)

def non_member(request):
    pass

def select_room(request):
     # 요구사항에 적합한 방들을 뽑아(현재 예약 날짜가 가능한 방들 -> reservation에 겹치는 날짜가 없는 방만)
    reservation = Reservation.objects.get(pk=reservation_pk)
    reservations = Reservation.objects.all()
    rooms = Room.objects.filter(room != reservations.room.filter(checkin=reservation.checkin))
    context = {
        'rooms': rooms
    }
    return render(request, 'reservations/select_room.html', context)
