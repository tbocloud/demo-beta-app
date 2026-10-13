# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

from frappe.model.document import Document

from beta_services.service.charges import visit_charge


class ServiceVisit(Document):
	def validate(self):
		self.charge = visit_charge(self.hours, self.rate_per_hour)

	def on_submit(self):
		self.db_set("status", "Completed")
