from django import forms
from .models import Agenda


class EventoForm(forms.ModelForm):
    descricao = forms.CharField(widget=forms.TextInput(attrs={'id':"TxtObservacoes"}))

    class Meta:
        model = Agenda
        fields = ('descricao',)


