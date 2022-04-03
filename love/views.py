from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Answer

def index(request):
    answer = Answer.objects.first()
    return render(request, 'love/index.html',{'answer': answer} )

def accept(request):
    if(Answer.objects.exists() == False):
        firstanswer = Answer(answer = True)
        firstanswer.save()

    return redirect('index')

def reject(request):
    if(Answer.objects.exists() == False):
        firstanswer = Answer(answer = False)
        firstanswer.save()

    return redirect('index')