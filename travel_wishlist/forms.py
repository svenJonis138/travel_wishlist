from django import forms
from .models import Place


class NewPlaceForm(forms.ModelForm):
    """ creates the form for entering a new place """
    class Meta:
        model = Place
        fields = ('name', 'visited')
