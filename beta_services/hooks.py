# Copyright (c) 2026, Team Back Office and contributors
# For license information, please see license.txt

app_name = "beta_services"
app_title = "Beta Services"
app_publisher = "Team Back Office"
app_description = "Maintenance contracts and service visits for Beta Services"
app_email = "support@teambackoffice.com"
app_license = "mit"
required_apps = ["erpnext"]

scheduler_events = {
	"daily": [
		"beta_services.service.planning.create_due_visits",
	],
}
