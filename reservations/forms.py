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
            'godfather' : 'Godfather',
            'student' : 'Student',
            #'dateTime' : 'Date Time',
        }
