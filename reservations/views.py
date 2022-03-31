from django.shortcuts import render
from .forms import ReservationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_reservation import create_reservation, get_reservations

def reservation_list(request):
    reservations = get_reservations()
    context = {
        'reservation_list': reservations
    }
    return render(request, 'Reservation/reservations.html', context)

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            create_reservation(form)
            messages.add_message(request, messages.SUCCESS, 'Reservation create successful')
            return HttpResponseRedirect(reverse('reservationCreate'))
        else:
            print(form.errors)
    else:
        form = ReservationForm()

    context = {
        'form': form,
    }

    return render(request, 'Reservation/reservationCreate.html', context)
