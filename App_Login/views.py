from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


from django.http import HttpResponse


#from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, logout, authenticate


#from App_Login.models import Profile
from App_Login.forms import DataEntryForm


from django.contrib import messages

def data_entry(request):
    form = DataEntryForm()
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully!")
            return HttpResponseRedirect(reverse('App_Login:DataEntryForm'))
    return render(request, 'App_Login/DataEntryForm.html', context={'form':form})
