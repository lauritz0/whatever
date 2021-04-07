from django.shortcuts import render
from django.http import HttpResponse
from .models import TelephoneBookEntry
# Create your views here.


def hello(request):
    return HttpResponse("Hello, World!")

def entries(request):
    entries = TelephoneBookEntry.objects.all()
    return render(request, 'entries.html', context={'entries': entries})

def test():
    return 'test'
