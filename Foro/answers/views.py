from django.shortcuts import render
from .forms import AnswerForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from .logic.answer_logic import create_answer, get_answers
import requests
import json

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

def AnswerList(request):
    queryset = Answer.objects.all()
    context = list(queryset.values('id', 'question', 'text', 'author', 'dateTime'))
    return JsonResponse(context, safe=False)

def AnswerCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        answer = answer()
        answer.question = data_json['question']
        answer.text = data_json['text']
        answer.author = data_json['author']
        answer.dateTime = data_json['dateTime']
        answer.save()
        return HttpResponse("successfully created answer")
    else:
        return HttpResponse("unsuccessfully created answer. Question does not exist")
