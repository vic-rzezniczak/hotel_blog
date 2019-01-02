from django.http import HttpResponse
import os



def index(request):
    return HttpResponse(f'Hello, world. You\'re at the {os.getcwd()} index.')