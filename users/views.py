from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from trversalapp.models import Trip
from forms import forms


def home(request):
	return render(request, 'landing.html')

class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class EditUserView(generic.UpdateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('mytrip_list')
    template_name = 'edit_user.html'

class MyTripList(generic.ListView):
    model = Trip
    template_name = 'my_trips.html'

    def get_queryset(self):
        return Trip.objects.filter(creator__username__exact=self.kwargs['username']).order_by('start_day')
        # return Trip.objects.filter(creator__username__exact='admin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_page"]=get_object_or_404(
            User, username=self.kwargs['username']
        )
        return context

class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'