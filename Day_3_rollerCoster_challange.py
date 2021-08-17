print("\n!!! Welcome to Roller Coaster Ride Kiosk!!!")

height = int(input("\nPlease ensure your height (cm): "))
bill = 0

if height >= 120:
    print("\nyou can ride! ")
    age = int(input("\nWhats' your age ? "))
    if age < 12:
        bill = 5
        print(f"You have to pay ${bill}")
    elif age <= 18:
        bill = 7
        print(f"You have to pay ${bill}")
    elif 45 <= age <= 55:
        print("\nYour Ride Is free!\n")
    else:
        bill = 12
        print(f"You have to pay ${bill}")

    want_photo = input("\nPlease conform if you want to be get capture? (y/n): ")

    if want_photo == "y":
        bill += 3
        print(f"\nYour final Bill for ride is : ${bill}")
    else:
        print(f"\nYour final bill is ${bill} enjoy ride !")

else:
    print("You cant' ride!")