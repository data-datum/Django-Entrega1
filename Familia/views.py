from django.shortcuts import render

from .models import Persona

# Create your views here.

def index(request):
    personas=Persona.objects.all()
    ctx = {'personas':personas}
    return render(request, "familia/index.html", ctx)