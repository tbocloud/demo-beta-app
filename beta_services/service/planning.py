# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""Planning the visits of the service contracts."""

import frappe
from frappe.utils import add_days, cint, getdate, today


def next_visit_date(last_visit, visits_per_year):
	"""The day the next visit is due: the year split evenly between the contract's visits."""
	return add_days(getdate(last_visit), 365 // max(cint(visits_per_year), 1))


def create_due_visits():
	"""Daily: plan the next visit of every active contract once it is due within a week."""
	horizon = getdate(add_days(today(), 7))
	contracts = frappe.get_all(
		"Service Contract",
		filters={"status": "Active"},
		fields=["name", "customer", "start_date", "end_date", "visits_per_year", "rate_per_hour"],
	)
	for contract in contracts:
		last = frappe.get_all(
			"Service Visit",
			filters={"contract": contract.name, "docstatus": ["<", 2]},
			fields=["visit_date"],
			order_by="visit_date desc",
			limit=1,
		)
		next_date = getdate(
			next_visit_date(last[0].visit_date if last else contract.start_date, contract.visits_per_year)
		)
		if next_date > contract.end_date:
			continue
		if next_date > horizon:
			continue
		if frappe.db.exists("Service Visit", {"contract": contract.name, "visit_date": next_date}):
			continue
		frappe.get_doc(
			{
				"doctype": "Service Visit",
				"contract": contract.name,
				"visit_date": next_date,
				"status": "Planned",
			}
		).insert(ignore_permissions=True)
