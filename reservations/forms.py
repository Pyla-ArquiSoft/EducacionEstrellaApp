from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'godfather',
            'student',
            #'dateTime',
        ]

        labels = {
            'godfather' : 'Padrino',
            'student' : 'Estudiante que pide la cita',
            #'dateTime' : 'Date Time',
        }
