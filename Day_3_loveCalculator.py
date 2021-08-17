print("!!! Welcome to Love Calculator!!!\n")

name1 = input("Please enter boy name: ")
name2 = input("Please enter girl name: ")

name_sum = name1 + name2

name_lower = name_sum.lower()

t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")

true = t + r + u + e

l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

love_score = int(love_score)

if 10 >= love_score <= 90:
    print(f"your score is {love_score}, you go together like coke and mentos.")
elif 40 >= love_score <= 55:
    print(f"your score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}.")