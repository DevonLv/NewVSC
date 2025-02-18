#POS charge calculator for wood signs

charge=35.00
numChars=float(input('Enter the number of characters: '))
color=input('Is the character color gold or black? ')
woodType=input('Is the sign made of oak or pine? ')

#calculate the price of the characters
if numChars=<5:
    charPrice=0
else:
    charPrice=(numChars-5)*4

final_charge=charge+charPrice+colorPrice+woodPrice
print(f'The charge for this sign is ${final_charge}')