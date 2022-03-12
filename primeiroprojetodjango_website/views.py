from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from primeiroprojetodjango_website.models import Pergunta
from primeiroprojetodjango_website.forms import PerguntaForm
# Create your views here.

def pergunta_form(request):
    if request.method == 'POST':
        form = PerguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = PerguntaForm()
        return render(request, "primeiroprojetodjango_website/pergunta_form.html", {'form': form})
        