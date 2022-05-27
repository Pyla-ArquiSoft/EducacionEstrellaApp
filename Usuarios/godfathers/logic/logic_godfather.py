from ..models import Godfather

def get_godfathers():
    queryset = Godfather.objects.all().order_by('-godStudent')[:10]
    return (queryset)

def create_godfather(form):
    godfather = form.save()
    godfather.save()
    return ()