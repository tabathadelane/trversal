from django import forms
from trversalapp.models import Trip

class NewTripForm(forms.ModelForm):
    
    class Meta:
        model = Trip
        fields = ["trip_name", "days_num", "start_day"]