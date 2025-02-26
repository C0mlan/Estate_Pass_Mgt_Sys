from django.forms import ModelForm
from .models import Guest



class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['flat_no','name', 'purpose']
