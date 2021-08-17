height = float(input("Enter your height (must be in meter): "))
weight = float(input("Enter you weight: "))

bmi = (weight / height ** 2)

bmi_int = round(bmi , 2)  # to convert float into integer usre of round to take round of

print("Your BMI is ", bmi_int)