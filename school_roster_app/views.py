# Create your views here.
# school_roster_app/views.py

from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    data={
        'all_group':my_school.staff
    }
    return render(request, 'pages/all_group.html', data)


def staff_detail(request, employee_id):
    data={
        'indiv':my_school.find_staff_by_id(employee_id)
    }
    return render(request, 'pages/individual.html', data)


def list_students(request):
    data={
        'all_group':my_school.students
    }
    return render(request, 'pages/all_group.html', data)


def student_detail(request, student_id):
    data={
        'indiv':my_school.find_student_by_id(student_id)
    }
    return render(request, 'pages/individual.html', data)