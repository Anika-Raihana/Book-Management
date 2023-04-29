from django.forms import ModelForm
from App_Login.models import User, Profile


from django.contrib.auth.forms import UserCreationForm

class DataEntryForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'publisher name', 'publisher age','page no.','publish date','type')
