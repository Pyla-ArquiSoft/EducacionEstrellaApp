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
            'question' : 'Question',
            'text' : 'Text',
            'author' : 'Author',
            #'dateTime' : 'Date Time',
        }
