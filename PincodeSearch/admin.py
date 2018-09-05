from django.contrib import admin

# Register your models here.
from PincodeSearch.models import PinCode, StateCode


admin.site.register(PinCode)
admin.site.register(StateCode)
