from ..models import Student

def get_students():
    queryset = Student.objects.all()
    return (queryset)

def create_student(form):
    question = form.save()
    question.save()
    return ()