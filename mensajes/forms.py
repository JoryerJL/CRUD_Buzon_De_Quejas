from .models import *
from django.forms import ModelForm
from django import forms


class mensajesModelForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = '__all__'

        labels = {
            'mensaje' : 'Descripcion',
            'fecha' : 'Fecha'
        }

        widgets = {
            'mensaje': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
