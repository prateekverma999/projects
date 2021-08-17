print("!!!Welcome to BMI Calculator!!!")

height = float(input("Please enter your height (Meter): "))
weight = float(input("Please enter your weight (Kg): "))

bmi = (weight / height ** 2)

bmi_round = round(bmi , 2)  # to convert float into integer usre of round to take round of

# print("Your BMI is ", bmi_round)

if bmi < 18.5:
    print(f"\nYour BMI is {bmi_round} you are under weight")
elif bmi <= 25:
    print(f"\nyour BMI is {bmi_round}, you have normal weight")
elif bmi <= 30:
    print(f"your BMI is {bmi_round}, you are overweight")
elif 30 < bmi < 35:
    print(f"\nyour BMI is {bmi_round}, you are obese")
else:
    print(f"\nyour BMI is {bmi_round}, you are clinically obese")

