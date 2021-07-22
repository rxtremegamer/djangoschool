from django.shortcuts import render
from django.http import HttpResponse
from .models import ExamScore


def HomePage(request):
    return render(request, 'school/home.html')

def ContactPage(request):
    return render(request, 'school/contact.html')

def AboutPage(request):
    return render(request, 'school/about.html')

def ShowScore(request):
    score = ExamScore.objects.all()
    context = {'score':score}
    return render(request, 'school/showscore.html', context)
