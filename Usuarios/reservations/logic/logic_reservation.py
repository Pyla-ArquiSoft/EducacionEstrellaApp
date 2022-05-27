from ..models import Reservation

def get_reservations():
    queryset = Reservation.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_reservation(form):
    reservation = form.save()
    reservation.save()
    return ()