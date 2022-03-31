from django import forms
from .models import Godfather

class GodfatherForm(forms.ModelForm):
    class Meta:
        model = Godfather
        fields = [
            'student',
            'godStudent',
        ]

        labels = {
            'student' : 'Estudiante apadrinado',
            'godStudent' : 'Estudiante padrino',
        }
