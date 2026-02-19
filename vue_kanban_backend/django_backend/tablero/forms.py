from django import forms
from .models import tablero_model

class TableroForm(forms.ModelForm):
    class Meta:
        model = tablero_model
        fields = [ 'guia', 'recibio', 'lista', 'desc', 'cliente', 'imagen']