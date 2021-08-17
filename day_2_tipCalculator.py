print("Welcome To Tip Calculator \n")

bill = float(input("Please enter the total bill amount: "))

tip = int(input("Please enter the tip percentage. (10%, 15% & 20%) : "))

split = int(input("Enter the number of persson you split in: "))

totalBill = ((bill * (tip / 100)) + bill) / split

totalBill = "{:0.2f}".format(totalBill)

# this function ["{:0.2f}".format(totalBill)] can be use for giving always 2 digits after decimal.

print(f"Each person must pay : {totalBill}")