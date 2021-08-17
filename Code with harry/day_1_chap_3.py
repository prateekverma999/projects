# a = input("Enter the name: ")
# b = input("Enter the date: ")
# letter = "Dear <|name|> \n You are selected ! \n <|date|>"
# letter = letter.replace("<|name|>", a)
# letter = letter.replace("<|date|>", b)
# print(letter)
string="Dear  a you are selected  for  the job"
print(string)
print(string.count("  "))
string=string.replace("  "," ")
print(string)