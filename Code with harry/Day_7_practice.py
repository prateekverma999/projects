# Dictionary function program

# myDict={
#     "durgesh":"lota",
#     "alka":"halka",
#     "prateek":"symbol",
#     "abhinandan":"vairagi"
# }
# print("please choose from the following option: ", myDict.keys())
# a = input("Please enter the Keys: ")
# print( "the meanning of the key is: ", myDict.get(a))
#_______________________________________________________________________________
# if else staement example

# num1 = int(input("enter the 1st number : "))
# num2 = int(input("enter the 2st number : "))
# num3 = int(input("enter the 3st number : "))
# num4 = int(input("enter the 4st number : "))

# # if(num1<num2):
# #     f1 = num1
# # else:
# #     f1 = num2

# # if(num3<num4):
# #     f2 = num3
# # else:
# #     f2 = num4

# # if(f1<f2):
# #     print(" Smallest numberb is : ", f1)
# # else:
# #     print(" Smallest numberb is : ", f2)


# if(num1<num2):
#     f1=num1
# else:
#     f1=num2

# if(f1<num3):
#     f1=f1
# else:
#     f1=num3

# if(f1<num4): 
#     f1=f1
# else:
#     f1=num4

# print("the smallest number is",f1)   


# question3
# a=input("enter the text")
# if("make a lot of money" in a):
#     spam=True
# elif("buy now" in a):
#     spam=True
# elif("subscribe this" in a):
#     spam=True
# else:
#     spam=False

# if(spam):
#     print(" this is spam  ")
# else:
#     print(" this is not spam")

# cheking string length

# a=input("enter the username : ")


# if((len(a))<10):
#     print("user name is less then 10 charecter")
# else:
#     print("user name more then 10 cherecter")


# cheking the item in the list

# a = input("Search name: ")

# list = ["alka", "durgesh", "prateek", "abhinandan", "hero"]

# if(a in list):
#     print("name present in the directory !!!")
# else:
#     print("!!! Name not found !!!")

# print the grade for marks:


# num1 = int(input("Enter the marks in math: "))
# num2 = int(input("enter the marks in english: "))
# num3 = int(input("enter the marks in hindi: "))
# num4 = int(input("enter the marks in sanskrit: "))

# a = (num1+num2+num3+num4)/4
# print("total Marks :", a)

# if(a>100):
#     print("Invalid entry !!")
# elif(a>=90):
#     garde = "Ex"
# elif(a>=80):
#     garde = "A"
# elif(a>=70):
#     garde = "B"
# elif(a>=60):
#     garde = "C"
# elif(a>=50):
#     garde = "D"
# else:
#     garde = "Fail"

# print("Your Grade is : ", garde)

# to serch the artical talk about the person or not


# artical = input("Write a artical: \n")

# a = input("enter the name you want to look for: ")

# if(a.upper() in artical.upper()):
#     print(" Artical Talking About Harry !")
# else:
#     print("Artical not talking about harry !")