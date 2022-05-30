from django.shortcuts import render
from questions.models import Question
from .forms import QuestionForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json
from .logic.logic_question import create_question, get_questions

def check_student(data):
    r = requests.get(settings.PATH_STUD, headers={"Accept":"application/json"})
    students = r.json() #Es neceario pasar student a json?
    for student in students:
        if data["student"] == student["id"]:
            return True
    return False

def question_list(request):
    questions = get_questions()
    context = {
        'question_list': questions
    }
    return render(request, 'Question/questions.html', context)

#def QuestionList(request):
#    queryset = Question.objects.all()
#    context = list(queryset.values('id', 'student_id', 'text', 'tag', 'dateTime'))
#    return JsonResponse(context, safe=False)

def QuestionCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_student(data_json) == True:
            question = question()
            question.student = data_json['student']
            question.text = data_json['text']
            question.tag = data_json['tag']
            question.dateTime = data_json['dateTime']
            question.save()
            return HttpResponse("successfully created question")
        else:
            return HttpResponse("unsuccessfully created question. Student does not exist")


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if (form.is_valid()):
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