from django.conf.urls import url


from PincodeSearch.api.views import (
	PinCodeListAPIView, PinCodeDetailAPIView,
	PinCodeDeleteAPIView, PinCodeUpdateAPIView,
	PinCodeCreateAPIView
	)

app_name = 'PincodeSearch'
urlpatterns = [
    url(r'^$', PinCodeListAPIView.as_view(), name="list"),
    url(r'^create/$', PinCodeCreateAPIView.as_view(), name="create"),
    url(r'^(?P<pincode>[\w-]+)/edit/$', PinCodeUpdateAPIView.as_view(), name="edit"),
    url(r'^(?P<pincode>[\w-]+)/delete/$', PinCodeDeleteAPIView.as_view(), name='delete'),
    url(r'^(?P<pincode>[\w-]+)/$', PinCodeDetailAPIView.as_view(), name='detail'),
]
