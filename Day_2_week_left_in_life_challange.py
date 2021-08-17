yourAge = int(input("Enter you age : "))

days = 365
week = 52
months = 12

age_left_days = (90 * days) - (yourAge * days)
age_left_week = (90 * week) - (yourAge * week)
age_left_months = (90 * months) - (yourAge * months)

print(f"You have {age_left_days} days, {age_left_week} weeks and {age_left_months} months left.")