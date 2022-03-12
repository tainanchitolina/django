from django import forms 
from primeiroprojetodjango_website.models import Pergunta

class PerguntaForm(forms.modelForm):
    class Meta:
        fields = ['enunciado']
        model = Pergunta