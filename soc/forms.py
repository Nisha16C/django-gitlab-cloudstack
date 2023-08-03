from django import forms
from .models import SOC

class SOCselection(forms.ModelForm):
    class Meta:
        model = SOC
        fields = ['SIEMxdr', 'monitoring', 'logging']