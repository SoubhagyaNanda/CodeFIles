from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    students = [
        {
        'name': 'Ravi gupta',
        'Profession': 'Youtuber'
        }
    ]
    return HttpResponse(students)