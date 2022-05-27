from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm
from .logic.student_logic import get_students, create_student

def student_list(request):
    students = get_students()
    context = {
        'student_list': students
    }
    return render(request, 'Student/students.html', context)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            create_student(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created student')
            return HttpResponseRedirect(reverse('studentCreate'))
        else:
            print(form.errors)
    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'Student/studentCreate.html', context)