# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

from frappe.tests.utils import FrappeTestCase

from beta_services.service.charges import visit_charge


class TestVisitCharge(FrappeTestCase):
	def test_hours_times_the_rate(self):
		self.assertEqual(visit_charge(1.5, 200), 300)

	def test_no_hours_no_charge(self):
		self.assertEqual(visit_charge(None, 200), 0)
