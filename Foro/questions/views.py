from django.shortcuts import render
from .forms import QuestionForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_question import create_question, get_questions

def question_list(request):
    questions = get_questions()
    context = {
        'question_list': questions
    }
    return render(request, 'Question/questions.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            create_question(form)
            messages.add_message(request, messages.SUCCESS, 'Question create successful')
            return HttpResponseRedirect(reverse('questionCreate'))
        else:
            print(form.errors)
    else:
        form = QuestionForm()

    context = {
        'form': form,
    }

    return render(request, 'Question/questionCreate.html', context)