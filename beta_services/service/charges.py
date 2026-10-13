# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

"""What a visit costs."""

from frappe.utils import flt


def visit_charge(hours, rate_per_hour) -> float:
	"""Hours on site times the contract's rate per hour."""
	return flt(flt(hours) * flt(rate_per_hour), 2)
