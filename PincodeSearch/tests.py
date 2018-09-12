from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
from .models import PinCode
from django.urls import reverse


class PinCodeTest(TestCase):

	"""
	This test is for models.
	"""

	def setUp(self):

		self.obj = PinCode.objects.create(place="New York",
			pincode="990033",
			office_Type="S.O",
			Delivery_status="Delivery",
			division_name="Georgia",
			region_name="9th Ave",
			circle_name="New York",
			Taluk="Brooklyn",
			district="Manhattan",
			state_name="New York",
				)
		return self.obj


	def test_pincode_create(self):

		w = self.setUp()
		self.assertTrue(isinstance(w, PinCode))
		self.assertEqual(w.place, "New York")
		self.assertEqual(w.pincode, "990033")
		self.assertEqual(w.office_Type, "S.O")
		self.assertEqual(w.Delivery_status, "Delivery")
		self.assertEqual(w.division_name, "Georgia")
		self.assertEqual(w.region_name, "9th Ave")
		self.assertEqual(w.circle_name, "New York")
		self.assertEqual(w.Taluk, "Brooklyn")
		self.assertEqual(w.district, "Manhattan")
		self.assertEqual(w.state_name, "New York")


class HomePageTests(TestCase):

	"""
	This test is for Home Page.
	"""

	def test_home_page(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)


	def test_view_url_by_name(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)


	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'searchpincode.html')

	def test_search_pincode(self):

		"""
		This test is to search pincode.
		"""

		search_pincode = "484001"
		res = self.client.put(
		reverse('search_pincode'),
			search_pincode
			)
		self.assertEqual(res.status_code, status.HTTP_200_OK)


class ViewTestCase(TestCase):
	"""
	Test for the api view.
	"""

	def setUp(self):

		self.client = APIClient()
		self.obj = PinCode.objects.create(place="New York",
			pincode="990033",
			office_Type="S.O",
			Delivery_status="Delivery",
			division_name="Georgia",
			region_name="9th Ave",
			circle_name="New York",
			Taluk="Brooklyn",
			district="Manhattan",
			state_name="New York",
				)
		return self.obj


	def test_api_can_create_a_pincode(self):

		"""
		Test the api has creation capability.
		"""

		self.create_pincode = {'place': 'New Place', "pincode": "899898",
			"office_Type": "New Office", "district": "Some District"
			}

		response = self.client.post(
			reverse('PincodeSearch-api:create'),
			self.create_pincode
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


	def test_api_can_get_details(self):

		"""
		Test the api can get a pincode details.
		"""

		pincode_data = self.setUp()
		response = self.client.get(
			reverse('PincodeSearch-api:details',
			kwargs={'pk': pincode_data.id}), format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_api_can_update_a_pincode(self):

		"""
		Test the api can update a pincode.
		"""

		pincode_data = self.setUp()
		change_pincode = {'place': 'New Place', "pincode": "899898",
			"office_Type": "New Office", "district": "Some District"
			}
		res = self.client.put(
		reverse('PincodeSearch-api:edit',
			kwargs={'pk': pincode_data.id}),
			change_pincode, format='json'
			)
		self.assertEqual(res.status_code, status.HTTP_200_OK)


	def test_api_can_delete_pincode(self):

		"""
		Test the api can delete a pincode.
		"""

		pincode_data = self.setUp()
		response = self.client.delete(
			reverse(
				'PincodeSearch-api:delete', kwargs={'pk': pincode_data.id}),
				format='json',
				follow=True
				)
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
