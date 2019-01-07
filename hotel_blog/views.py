from django.http import HttpResponse
import os



def index(request):
    return HttpResponse(f'Hello, world. You\'re at the {os.getcwd()} index.')


def detail(request, question_id):
    return HttpResponse(f'You\'re looking at question {question_id}.')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}.')