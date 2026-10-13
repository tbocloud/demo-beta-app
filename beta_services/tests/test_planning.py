# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

from datetime import date

from frappe.tests.utils import FrappeTestCase

from beta_services.service.planning import next_visit_date


class TestPlanning(FrappeTestCase):
	def test_four_visits_a_year_are_a_quarter_apart(self):
		self.assertEqual(str(next_visit_date(date(2026, 1, 1), 4)), "2026-04-02")

	def test_monthly_visits(self):
		self.assertEqual(str(next_visit_date(date(2026, 1, 1), 12)), "2026-01-31")
