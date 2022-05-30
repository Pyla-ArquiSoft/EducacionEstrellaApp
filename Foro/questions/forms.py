from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'student_id',
            'text',
            'tag',
            #'dateTime',
        ]

        labels = {
            'student_id' : 'Estudiante',
            'text' : 'Texto',
            'tag' : 'Tag',
            #'dateTime' : 'Date Time',
        }
