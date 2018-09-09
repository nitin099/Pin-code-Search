from rest_framework.serializers import ModelSerializer

from PincodeSearch.models import PinCode



# Single serualizer for CRUD application.

class PinCodeSerializer(ModelSerializer):
	class Meta:
		model = PinCode
		fields = [
			'id',
			'place',
			"pincode",
			'office_Type',
			'Delivery_status',
			'division_name',
			"region_name",
			"circle_name",
			"Taluk",
			'district',
			"state_name",
		]
