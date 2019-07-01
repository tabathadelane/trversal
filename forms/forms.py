from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from trversalapp.models import Trip, Day, Location


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class NewTripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ["name", "start_day"]
        widgets = {
            "start_day": forms.TextInput(attrs={"type":"date"})
        }
    
    def __init__(self, *args, **kwargs):
        super(NewTripForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name your trip:"
        self.fields['start_day'].label = "What day does your trip begin?"


class NewDayForm(forms.ModelForm):
    
    class Meta:
        model = Day
        fields = ["start_time", "mode"]
        widgets = {
            "start_time_hour": forms.TextInput(attrs={"type":"time"})
        }

class NewLocForm(forms.ModelForm):
    auto_id = False 
    g_name = forms.CharField(label="", widget=forms.TextInput(attrs={'id':'autocomplete', "placeholder":"Enter a new Location" }))

    class Meta:
        model = Location
        fields = ["g_name", "duration_hour", "duration_min"]
        duration_hour = forms.Field(label="Hours", widget=forms.TextInput(attrs={"type":"select"}))

    def __init__(self, *args, **kwargs):
        super(NewLocForm, self).__init__(*args, **kwargs)
        self.fields['duration_hour'].label = "How long do you think you'll be there?"
        self.fields['duration_min'].label = ""
        