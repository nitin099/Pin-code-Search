from django.shortcuts import render
import json
from django.http import Http404
import requests
# Create your views here.
from .models import PinCode
from django.db.models import Q
from .forms import PincodeForm, SearchForm


def home(request):
	form  = PincodeForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, "home.html", context)


# def search(request):
# 	form = SearchForm(request.POST or None)
# 	if form.is_valid():
# 		pincode = form.cleaned_data.get('pincode')
# 		print(pincode)
# 		url = "http://postalpincode.in/api/pincode/%s" % pincode
# 		response = requests.get(url)
# 		result = response.json()
# 		print(result,"$$$$$$$$$$$$$$$$$")
# 		print(json.dumps(result, indent=4))
# 		print (type(result))
# 		try:
# 			state = result["PostOffice"][0]["State"]
# 			district = result["PostOffice"][0]["District"]
# 			circle = result["PostOffice"][0]["Circle"]
# 			context = {
# 			'form': form,
# 			'state': state,
# 			"district": district,
# 			"circle": circle
# 			}
# 			return render(request, "searchpincode.html", context)
# 		except:
# 			return render(request, "searchpincode.html", {"invalid":"Invalid Pincode"})
# 	return render(request,'searchpincode.html', {"form": form})	


def search(request):
	form = PincodeForm(request.POST or None)
	queryset_list = PinCode.objects.all()
	query = request.GET.get("q")
	if query:
		queryset = queryset_list.filter(
			Q(pincode__icontains=query)|
			Q(place__iexact=query)|
			Q(district__iexact=query)|
			Q(state_name__icontains=query)
			).distinct()
		context = {
			"form": form,
			"queryset": queryset
		}
		return render(request, "searchpincode.html", context)
	context ={
		'form': form,
	}
	return render(request, "searchpincode.html", context)