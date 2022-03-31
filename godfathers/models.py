from django.db import models
from students.models import Student


class Godfather(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    godStudent = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s' % (self.student, self.godStudent)