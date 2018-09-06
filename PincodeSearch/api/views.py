from rest_framework.generics import (
	ListAPIView, RetrieveAPIView,
	UpdateAPIView, DestroyAPIView,
	CreateAPIView
	)
from django.db.models import Q
from PincodeSearch.models import PinCode
from .serializers import PinCodeSerializer, PinCodeCreateSerializer


class PinCodeCreateAPIView(CreateAPIView):
	queryset = PinCode.objects.all()
	serializer_class = PinCodeSerializer


class PinCodeDetailAPIView(RetrieveAPIView):
	queryset = PinCode.objects.all()
	serializer_class = PinCodeSerializer
	lookup_field  = 'pincode'
	lookup_url_kwarg = "pincode"


class PinCodeDeleteAPIView(DestroyAPIView):
	queryset = PinCode.objects.all()
	serializer_class = PinCodeSerializer
	lookup_field  = 'place'
	#lookup_url_kwarg = "abc"


class PinCodeUpdateAPIView(UpdateAPIView):
	queryset = PinCode.objects.all()
	serializer_class = PinCodeSerializer
	lookup_field  = 'pincode'
	#lookup_url_kwarg = "abc"


class PinCodeListAPIView(ListAPIView):
	serializer_class = PinCodeSerializer

	def get_queryset(self, *args, **kwargs):
		queryset_list = PinCode.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(pincode__icontains=query)|
				Q(place__iexact=query)|
				Q(district__iexact=query)|
				Q(state_name__icontains=query)
				).distinct()
		return queryset_list

