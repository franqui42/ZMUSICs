from django import forms
from.models import *

class contacto_form(forms.Form):
    correo = forms.EmailField(widget= forms.TextInput())
    titulo = forms.CharField(widget= forms.TextInput())
    texto = forms.CharField(widget= forms.Textarea())


class agregar_album_form(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'