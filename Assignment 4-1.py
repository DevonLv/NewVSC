#POS charge calculator for wood signs

#declare variables and gain inputs from User
charge=35.00
numChars=float(input('Enter the number of characters: '))
woodType=input('Is the sign made of oak or pine? ')
color=input('Is the character color gold or black/white? ')

#calculate the price of the characters
if numChars<=5:
    charPrice=0
else:
    charPrice=(numChars-5)*4.00

#calculate the price of the color
if color=='gold':
    colorPrice=15.00
else:
    colorPrice=0

#calculate the price of the wood
if woodType=='oak':
    woodPrice=20.00
else:
    woodPrice=0

#calculate the final total charge
final_charge=charge+charPrice+colorPrice+woodPrice

#display final charge
print(f'The charge for this sign is ${final_charge}')