from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "primeiroprojetodjango_website/home.html",
        {"hello": "Beep, Beep, Beeeep! I'm alive!" })