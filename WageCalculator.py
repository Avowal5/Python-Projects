hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
week_day = input("Day of the week: ")
daily_wage = hourly_wage * hours_worked


if week_day == "Sunday":
    print(f"Daily wages: {hourly_wage * 2 * hours_worked} euros")

if week_day != "Sunday":
    print(f"Daily wages: {hourly_wage * hours_worked} euros")