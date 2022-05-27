from django.db import models
from students.models import Student


class Question(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    text = models.CharField(max_length=1000)
    #Implementar tags despues si se puede
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.student, self.text)