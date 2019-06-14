from django import forms
from trversalapp.models import Trip, Day, Location

class NewTripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ["name", "days_num", "start_day"]
        widgets = {
            "start_day": forms.TextInput(attrs={"type":"date"})
        }

class NewDayForm(forms.ModelForm):
    
    class Meta:
        model = Day
        fields = ["start_time", "day_order",]
        widgets = {
            "start_time_hour": forms.TextInput(attrs={"type":"time"})
        }

class NewLocForm(forms.ModelForm):
    auto_id = False 
    g_name = forms.CharField(label="", widget=forms.Textarea(attrs={'id':'autocomplete', "placeholder":"Enter a Location" }))

    class Meta:
        model = Location
        fields = ["g_name", "duration_hour", "duration_min", "order",]