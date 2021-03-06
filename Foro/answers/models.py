from django.db import models
from questions.models import Question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    text = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000, default="")
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.question, self.text)