from django import forms
from .models import Resident, Blotter, Certificate

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'


class BlotterForm(forms.ModelForm):
    class Meta:
        model = Blotter
        fields = '__all__'


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'