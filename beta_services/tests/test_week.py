# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

from datetime import date

from frappe.tests.utils import FrappeTestCase

from beta_services.beta_services.report.visits_due_this_week.visits_due_this_week import week_bounds


class TestWeek(FrappeTestCase):
	def test_a_wednesday_belongs_to_its_monday_to_sunday(self):
		self.assertEqual(week_bounds(date(2026, 10, 14)), (date(2026, 10, 12), date(2026, 10, 18)))

	def test_a_monday_starts_its_own_week(self):
		self.assertEqual(week_bounds(date(2026, 10, 12))[0], date(2026, 10, 12))
