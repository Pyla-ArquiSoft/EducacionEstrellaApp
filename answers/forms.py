from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'question',
            'text',
            #'dateTime',
        ]

        labels = {
            'question' : 'Question',
            'text' : 'Text',
            #'dateTime' : 'Date Time',
        }
