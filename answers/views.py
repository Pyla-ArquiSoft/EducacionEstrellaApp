from django.shortcuts import render
from .forms import AnswerForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.answer_logic import create_answer, get_answers

def answer_list(request):
    answers = get_answers()
    context = {
        'answer_list': answers
    }
    return render(request, 'Answer/answers.html', context)

def answer_create(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            create_answer(form)
            messages.add_message(request, messages.SUCCESS, 'Answer create successful')
            return HttpResponseRedirect(reverse('answercreate'))
        else:
            print(form.errors)
    else:
        form = AnswerForm()

    context = {
        'form': form,
    }

    return render(request, 'Answer/answerCreate.html', context)
