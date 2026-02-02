from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import CustomerInquiry
from apps.locations.models import Province, District


class CustomerInquirySubmissionTests(TestCase):
	def setUp(self):
		self.province_a = Province.objects.create(
			name_th="กรุงเทพมหานคร",
			name_en="Bangkok",
			geography_id=2,
		)
		self.province_b = Province.objects.create(
			name_th="เชียงใหม่",
			name_en="Chiang Mai",
			geography_id=1,
		)
		self.district_a1 = District.objects.create(
			province=self.province_a,
			name_th="บางเขน",
			name_en="Bang Khen",
		)
		self.district_b1 = District.objects.create(
			province=self.province_b,
			name_th="เมืองเชียงใหม่",
			name_en="Mueang Chiang Mai",
		)

	def _valid_payload(self, province=None, district=None, **overrides):
		data = {
			"first_name": "Somchai",
			"last_name": "Jaidee",
			"phone": "0812345678",
			"line_id": "somchai.line",
			"province": (province or self.province_a).id,
			"district": (district or self.district_a1).id,
			"address_detail": "123/45 ถนนสุขุมวิท",
			"budget": CustomerInquiry.BUDGET_CHOICES[0][0],
			"preferred_day": CustomerInquiry.DAY_CHOICES[0][0],
			"preferred_time": CustomerInquiry.TIME_CHOICES[0][0],
			"note": "ทดสอบระบบ",
		}
		data.update(overrides)
		return data

	def test_submit_inquiry_success_creates_record(self):
		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=self._valid_payload(),
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 1)
		self.assertTemplateUsed(response, "accounts/partials/success_message.html")
		self.assertContains(response, "ส่งข้อมูลสำเร็จ!")
		self.assertContains(response, "hx-swap-oob=\"outerHTML\"")

	def test_submit_inquiry_missing_required_fields_returns_error(self):
		payload = self._valid_payload()
		payload.pop("budget")

		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=payload,
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 0)
		self.assertTemplateUsed(response, "accounts/partials/error_message.html")
		self.assertContains(response, "กรุณาตรวจสอบข้อมูล")

	def test_submit_inquiry_requires_post_method(self):
		response = self.client.get(reverse("accounts:submit_inquiry"))

		self.assertEqual(response.status_code, 405)
		self.assertEqual(CustomerInquiry.objects.count(), 0)

	def test_submit_inquiry_missing_preferred_time_returns_error(self):
		payload = self._valid_payload()
		payload.pop("preferred_time")

		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=payload,
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 0)
		self.assertTemplateUsed(response, "accounts/partials/error_message.html")

	def test_submit_inquiry_allows_optional_fields_blank(self):
		payload = self._valid_payload(line_id="", address_detail="", note="")

		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=payload,
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 1)
		inquiry = CustomerInquiry.objects.first()
		self.assertEqual(inquiry.line_id, "")
		self.assertEqual(inquiry.address_detail, "")
		self.assertEqual(inquiry.note, "")

	def test_submit_inquiry_rejects_district_not_in_province(self):
		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=self._valid_payload(
				province=self.province_a,
				district=self.district_b1,
			),
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 0)
		self.assertTemplateUsed(response, "accounts/partials/error_message.html")

	def test_submit_inquiry_rejects_unknown_province(self):
		payload = self._valid_payload()
		payload["province"] = 999999

		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=payload,
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 0)
		self.assertTemplateUsed(response, "accounts/partials/error_message.html")

	def test_submit_inquiry_rejects_unknown_district(self):
		payload = self._valid_payload()
		payload["district"] = 999999

		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=payload,
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 0)
		self.assertTemplateUsed(response, "accounts/partials/error_message.html")

	def test_submit_inquiry_rejects_phone_without_leading_zero(self):
		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=self._valid_payload(phone="9123456789"),
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 0)
		self.assertTemplateUsed(response, "accounts/partials/error_message.html")

	def test_submit_inquiry_rejects_phone_not_10_digits(self):
		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=self._valid_payload(phone="081234567"),
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 0)
		self.assertTemplateUsed(response, "accounts/partials/error_message.html")

	def test_submit_inquiry_normalizes_phone_digits(self):
		response = self.client.post(
			reverse("accounts:submit_inquiry"),
			data=self._valid_payload(phone="081-234-5678"),
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(CustomerInquiry.objects.count(), 1)
		inquiry = CustomerInquiry.objects.first()
		self.assertEqual(inquiry.phone, "0812345678")

	def test_get_districts_filters_by_province(self):
		response = self.client.get(
			reverse("accounts:get_districts"),
			data={"province": self.province_a.id},
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.district_a1.name_th)
		self.assertNotContains(response, self.district_b1.name_th)

	def test_get_districts_without_province_returns_placeholder_only(self):
		response = self.client.get(
			reverse("accounts:get_districts"),
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "กรุณาเลือกอำเภอ/เขต")
		self.assertNotContains(response, self.district_a1.name_th)
		self.assertNotContains(response, self.district_b1.name_th)

	def test_get_districts_invalid_province_returns_placeholder_only(self):
		response = self.client.get(
			reverse("accounts:get_districts"),
			data={"province": 999999},
			HTTP_HX_REQUEST="true",
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "กรุณาเลือกอำเภอ/เขต")
		self.assertNotContains(response, self.district_a1.name_th)
		self.assertNotContains(response, self.district_b1.name_th)
