from django.shortcuts import render
from django.http import HttpResponse
from.models import Team

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def teams(request):
    return render(request, 'teams.html')
