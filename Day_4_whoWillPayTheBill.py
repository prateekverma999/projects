import random

name_list = input("Give me everybody's names, separated by a comma. : ")
name = name_list.split(", ")

# ********************************************************************************
# name_items = len(name)
#
# random_choice = random.randint(0, name_items - 1)
#
# person_pay_bill = name[random_choice]
# ********************************************************************************


person_pay_bill = random.choice(name)

print(f"{person_pay_bill} is going to buy the meal today!")

'''
# we can use either code using random module.
# random.randint()
# random.choice()
'''
# lst = [3,4,1,6,2]
# lst[1:2]=[7,8]
# print(lst)