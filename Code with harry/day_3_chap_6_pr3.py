a=input("enter the text")
if("make a lot of money" in a):
    spam=True
elif("buy now" in a):
    spam=True
elif("subscribe this" in a):
    spam=True
else:
    spam=False

if(spam):
    print(" this is spam  ")
else:
    print(" thins is prank")