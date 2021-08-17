print("!!! Welcome to Leap year search!!!")

year = int(input("Enter a year to determine: "))

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("leap year")
else:
    print("Not Leap year")