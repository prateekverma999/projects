# print("!!! Welcome To Leap Year Predictor")
#
year = int(input("Please enter the year to predict: "))
#
# leap = False
#
# if year % 400 == 0:
#     leap = True
#     print("leap year!")
# elif year % 100 == 0:
#     leap = False
#     print("NOT! leap year")
# elif year % 4 == 0:
#     leap = True
#     print("Leap Year")
#
# print(f"\n{year} is a leap year? {leap}")

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} Leap year.")
else:
    print(f"{year} Not leap year.")