# Beta Services

The custom app of **Beta Services**, a maintenance company with yearly service contracts and field visits, on ERPNext 15.

Beta Services is a fictional company used to test TBO Support. This repository holds no real customer code or data.

## What it adds

- **Service Contract.** A customer's maintenance contract: start and end dates (no end date for a contract that runs until cancelled), visits per year and the rate per hour.
- **Service Visit.** A visit under a contract: date, technician, hours on site and the charge (hours × the contract's rate). A visit is submitted when completed.
- **Visit planning.** Every day the next visit of each active contract is planned once it is due within a week; the year is split evenly between the contract's visits.
- **Visits Due This Week.** A report of the visits from Monday to Sunday of a chosen week.

## Install

```
bench get-app https://github.com/tbocloud/demo-beta-app
bench --site <site> install-app beta_services
```

ERPNext 15 is required.

## Tests

```
bench --site <site> run-tests --app beta_services
```
