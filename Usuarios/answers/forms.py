from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'question',
            'text',
            'author',
            #'dateTime',
        ]

        labels = {
            'question' : 'Pregunta',
            'text' : 'Texto',
            'author' : 'Autor',
            #'dateTime' : 'Date Time',
        }
