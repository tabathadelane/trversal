from django import forms
from trversalapp.models import Day

class NewDayForm(forms.ModelForm):
    
    class Meta:
        model = Day
        fields = ["start_time", "day_date",]