print("!!!Welcome to Pizza Kiosk!!!\n\nChoose your selection from bellow :-p")

pizzaSize = int(input("1. Small Pizza\n2. Medium Pizza\n3. Large Pizza\n"))
bill = 0

if pizzaSize == 1:
    print("You select Small Pizza, you bill is $15")
    bill = 15
elif pizzaSize == 2:
    print("You select Medium Pizza, you bill is $20")
    bill = 20
elif pizzaSize == 3:
    print("You select Large Pizza, you bill is $25")
    bill = 25

add_pepperoni = input("\nDo you want pepperoni? y/n : ")
if add_pepperoni == "y" and "Y":
    if pizzaSize == 1:
        print("Extra $2 added")
        bill += 2
    else:
        print("Extra $3 added")
        bill += 3

extra_cheese = input("\nDo you want extra cheese ? y/n : ")
if extra_cheese == "y" and "Y":
    print("Extra $1 added")
    bill += 1
    print(f"\nYour final billing is: ${bill}")
else:
    print(f"\nYour Final Bill Is: ${bill}")