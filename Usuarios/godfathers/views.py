from django.shortcuts import render
from .forms import GodfatherForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_godfather import create_godfather, get_godfathers

def godfather_list(request):
    godfathers = get_godfathers()
    context = {
        'godfather_list': godfathers
    }
    return render(request, 'Godfather/godfathers.html', context)

def godfather_create(request):
    if request.method == 'POST':
        form = GodfatherForm(request.POST)
        if form.is_valid():
            create_godfather(form)
            messages.add_message(request, messages.SUCCESS, 'Godfather create successful')
            return HttpResponseRedirect(reverse('godfatherCreate'))
        else:
            print(form.errors)
    else:
        form = GodfatherForm()

    context = {
        'form': form,
    }

    return render(request, 'Godfather/godfatherCreate.html', context)