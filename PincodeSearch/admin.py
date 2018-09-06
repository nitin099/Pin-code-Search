from django.contrib import admin

# Register your models here.
from PincodeSearch.models import PinCode

class PinCodeAdmin(admin.ModelAdmin):
	list_display = ["place", 'pincode',"office_Type", "Delivery_status", 
			"division_name", "region_name", "circle_name", 'Taluk', "district", "state_name"]
	
	# list_filter = ["updated", "timestamp"]
	search_fields = ["place", 'pincode',
			"district", "state_name"]
	#list_display_links = ["palce"]
	#list_editable = ["title"]
	
	class Meta:
		model = PinCode

admin.site.register(PinCode, PinCodeAdmin)
