from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from .models import Student
from .forms import StudentForm
from .logic.student_logic import get_students, create_student
import json

def student_list(request):
    students = get_students()
    context = {
        'student_list': students
    }
    return render(request, 'Student/students.html', context)

def studentCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        student = Student()
        student.name = data_json["name"]
        student.save()
        return HttpResponse("successfully created student")

def studentList(request):
    queryset = Student.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            create_student(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created student')
            return HttpResponseRedirect(reverse('student_create'))
        else:
            print(form.errors)
    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'Student/studentCreate.html', context)