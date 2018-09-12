from django.shortcuts import render
import json
from django.http import Http404
import requests
from .models import PinCode
from django.db.models import Q
from .forms import PincodeForm, SearchForm

# Create your views here.

def home(request):
	form  = PincodeForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, "home.html", context)


def search(request):
	not_found = "No results found"
	form = PincodeForm(request.POST or None)
	queryset_list = PinCode.objects.all()
	query = request.GET.get("q")
	if query:
		query = query.strip()
		queryset = queryset_list.filter(
			Q(pincode__icontains=query)|
			Q(place__icontains=query)|
			Q(district__icontains=query)|
			Q(state_name__icontains=query)
			).distinct()
		context = {
			"form": form,
			"queryset": queryset,
			"not_found": not_found
		}
		return render(request, "searchpincode.html", context)
	context ={
		'form': form,
	}
	return render(request, "searchpincode.html", context)
