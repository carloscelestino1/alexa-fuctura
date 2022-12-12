from django import forms
from .models import Evento


class EventoForm(forms.ModelForm):
    data = forms.DateTimeField(
        label='Início do evento',
        widget=forms.DateTimeInput(
            format='%Y-%m-%d T%H:%M',
            attrs={
                'type': 'datetime-local',
            }),
        input_formats=('%Y-%m-%d T%H:%M',))

    class Meta:
        model = Evento
        fields = ('data', 'descricao', 'link')


