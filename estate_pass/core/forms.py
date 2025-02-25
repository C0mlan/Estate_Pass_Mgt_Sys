from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Guest


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['flat_no','name', 'purpose']