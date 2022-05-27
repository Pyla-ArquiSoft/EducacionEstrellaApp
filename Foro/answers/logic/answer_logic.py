from ..models import Answer

def get_answers():
    queryset = Answer.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_answer(form):
    answer = form.save()
    answer.save()
    return ()