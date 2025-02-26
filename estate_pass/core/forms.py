from django.forms import ModelForm
from .models import Guest



class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = [ 'name', 'purpose']
