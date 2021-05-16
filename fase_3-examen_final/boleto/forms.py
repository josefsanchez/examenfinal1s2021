from django import forms
from django.forms import fields
from django.forms.fields import CharField, IntegerField, DecimalField
from django.forms.formsets import MAX_NUM_FORM_COUNT
from django.forms import ModelForm, models
from .models import Boleto

class BoletoForm(forms.Form):
    clase   = forms.IntegerField(min_value=1, max_value=3, required=True)
    comida  = forms.IntegerField(min_value=0, max_value=100)
    bebida  = forms.IntegerField(min_value=0, max_value=100)
    pelicula= forms.IntegerField(min_value=0, max_value=100)

class TotalForm(forms.ModelForm):
    subtotal    = forms.IntegerField(initial=0)
    descuento   = forms.IntegerField(initial=0)
    total       = forms.DecimalField(initial=0)
    class Meta:
        model=Boleto
        fields = (
            'subtotal',
            'descuento',
            'total'
          )