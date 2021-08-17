sub1=int(input("enter sub1 marks"))
sub2=int(input("enter sub2 marks"))
sub3=int(input("enter sub3 marks"))

if(sub1<33 and sub2<33 and sub3<33):
    print("you are fail")
elif(sub1+sub2+sub3)/3<40:
    print("you are fail")
else:
    print("you are pass")