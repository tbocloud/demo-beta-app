# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""The visits from Monday to Sunday of a week."""

import frappe
from frappe import _
from frappe.utils import add_days, getdate, today


def week_bounds(day):
	"""Monday and Sunday of the week `day` falls in."""
	day = getdate(day)
	monday = add_days(day, -day.weekday())
	return getdate(monday), getdate(add_days(monday, 6))


def execute(filters=None):
	filters = filters or {}
	monday, sunday = week_bounds(filters.get("week") or today())
	data = frappe.get_all(
		"Service Visit",
		filters=[
			["visit_date", ">=", monday],
			["visit_date", "<", sunday],
			["docstatus", "<", 2],
		],
		fields=["name", "visit_date", "customer", "contract", "technician", "status"],
		order_by="visit_date asc",
	)
	columns = [
		{
			"fieldname": "name",
			"label": _("Visit"),
			"fieldtype": "Link",
			"options": "Service Visit",
			"width": 150,
		},
		{"fieldname": "visit_date", "label": _("Date"), "fieldtype": "Date", "width": 110},
		{
			"fieldname": "customer",
			"label": _("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"width": 180,
		},
		{
			"fieldname": "contract",
			"label": _("Contract"),
			"fieldtype": "Link",
			"options": "Service Contract",
			"width": 140,
		},
		{"fieldname": "technician", "label": _("Technician"), "fieldtype": "Data", "width": 140},
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
	]
	return columns, data
