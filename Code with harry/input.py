letter ='''Dear <|NAME|>,
 YOU ARE SELECTED !
 <|date|>'''
 
name = input('enter your name')
date = input('enter the date')

letter = letter.replace('<|NAME|>' , name)
letter = letter.replace('<|date|>' , date)

print(letter)
