from django import forms 
from primeiroprojetodjango_website.models import Pergunta

class PerguntaForm(forms.ModelForm):
  class Meta:
    fields = ['enunciado']
    model = Pergunta 
