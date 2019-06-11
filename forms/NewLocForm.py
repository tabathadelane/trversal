from django import forms
from trversalapp.models import Location

class NewLocForm(forms.ModelForm):
    auto_id = False 
    name = forms.CharField(label="", widget=forms.Textarea(attrs={'id':'autocomplete', "placeholder":"Enter a Location" }))

    class Meta:
        model = Location
        fields = ["name", "duration_hour", "duration_min", "order",]