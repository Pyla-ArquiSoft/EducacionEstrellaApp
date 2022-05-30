from django.db import models


class Question(models.Model):
    TAGS = (
        ('EDU', 'Educacion'),
        ('FOR', 'Foraneo'),
        ('FIN', 'Financiacion'),
    )
    student_id = models.IntegerField(null=False, default=None)
    text = models.CharField(max_length=1000)
    tag = models.CharField(max_length=50, choices=TAGS)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.student, self.text)