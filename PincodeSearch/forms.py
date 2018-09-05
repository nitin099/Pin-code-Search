from django import forms
from .models import PinCode, StateCode


class PincodeForm(forms.ModelForm):
    class Meta:
        model = PinCode
        fields = '__all__'

    state = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=StateCode.objects.all(),
        )
    
    place = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=PinCode.objects.all(),
        )

class SearchForm(forms.Form):
	pincode = forms.CharField(max_length=20)
