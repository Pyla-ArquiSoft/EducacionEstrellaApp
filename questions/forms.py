from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'student',
            'text',
            #'dateTime',
        ]

        labels = {
            'student' : 'Estudiante',
            'text' : 'Texto',
            #'dateTime' : 'Date Time',
        }
