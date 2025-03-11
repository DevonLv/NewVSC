# Taxes -
# TAX_RATE
TAX_RATE=0.13
RATE_OF_DEDUCTION=2000

def calculate_tax(tax_rate):
    # calculate tax bill (gross_income * TAX_RATE)
tax_bill=gross_income * TAX_RATE

##calculate rate of deduction
dependent_deduction = RATE_OF_DEDUCTION * num_of_dependents

#calculate tax subtotal
tax_subtotal = tax_bill - dependent_deduction

return tax_subtotal

while (True):
    # get dependents
    num_of_dependents = float(input("Enter number of dependents: "))
    
    #get gross income
    gross_income = float(input("Enter your gross income: "))
    
    #get state
    state_code = input("Enter your two digit state code: ")
    
    if (state_code == 'CA'):
        #print tax total
        print(f'Your tax bill is: ${calculate_tax(TAX_RATE)}')
    elif (state_code == 'NY'):
        # print tax subtotal
        print(f'Your tax subtotal is: ${calculate_tax(0.109)}')
        continue
    else:
        print(f'Your state does not have an income tax, praise the Emperor!')
    
    stop = input("Would you like to calculate another tax bill? (y/n): ")
    if (stop == 'n'):
        break
    