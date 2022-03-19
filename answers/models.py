from django.db import models
from students.models import Student
from questions.models import Question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    text = models.CharField(max_length=1000)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.question, self.text)