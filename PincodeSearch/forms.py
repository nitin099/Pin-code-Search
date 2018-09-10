from django import forms
from .models import PinCode


class PincodeForm(forms.ModelForm):
    class Meta:
        model = PinCode
        fields = '__all__'

    place = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=PinCode.objects.all(),
        )

class SearchForm(forms.Form):
	pincode = forms.CharField(max_length=20)
