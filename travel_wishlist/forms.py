from django import forms
from .models import Place


class NewPlaceForm(forms.ModelForm):
    """ creates the form for entering a new place """
    class Meta:
        model = Place
        fields = ('name', 'visited')


class DateInput(forms.DateInput):
    """ creates a date widget to select the date a place was visited """
    input_type = 'date'


class TripReviewForm(forms.ModelForm):
    """ creates a form to save notes and a picture along with the date visited """
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput()
        }