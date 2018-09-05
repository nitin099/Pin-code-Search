from django.shortcuts import render
import json
from django.http import Http404
import requests
# Create your views here.
from .forms import PincodeForm, SearchForm


def home(request):
	form  = PincodeForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, "home.html", context)


def search(request):
	form = SearchForm(request.POST or None)
	if form.is_valid():
		pincode = form.cleaned_data.get('pincode')
		print(pincode)
		url = "http://postalpincode.in/api/pincode/%s" % pincode
		response = requests.get(url)
		result = response.json()
		print(result,"$$$$$$$$$$$$$$$$$")
		print(json.dumps(result, indent=4))
		print (type(result))
		try:
			state = result["PostOffice"][0]["State"]
			district = result["PostOffice"][0]["District"]
			circle = result["PostOffice"][0]["Circle"]
			context = {
			'form': form,
			'state': state,
			"district": district,
			"circle": circle
			}
			return render(request, "searchpincode.html", context)
		except:
			return render(request, "searchpincode.html", {"invalid":"Invalid Pincode"})
	return render(request,'searchpincode.html', {"form": form})	