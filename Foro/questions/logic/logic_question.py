from ..models import Question

def get_questions():
    queryset = Question.objects.all()
    return (queryset)

def create_question(form):
    question = form.save()
    question.save()
    return ()