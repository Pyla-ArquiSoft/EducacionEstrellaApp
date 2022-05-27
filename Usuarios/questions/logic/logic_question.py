from ..models import Question

def get_questions():
    queryset = Question.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_question(form):
    question = form.save()
    question.save()
    return ()