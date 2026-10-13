// Copyright (c) 2026, Team Back Office and contributors
// For license information, please see license.txt

frappe.query_reports["Visits Due This Week"] = {
	filters: [
		{
			fieldname: "week",
			label: __("Any Day of the Week"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
		},
	],
};
