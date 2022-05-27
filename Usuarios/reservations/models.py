from django.db import models
from students.models import Student


class Reservation(models.Model):
    godfather = models.CharField(max_length=1000)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.godfather, self.student)