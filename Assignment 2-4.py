stateTaxRate = 0.065
federalTaxRate = 0.28
salary = input("Enter your salary: ")
stateTax = float(salary) * stateTaxRate
federalTax = float(salary) * federalTaxRate
numDependents = input("Enter the number of dependents: ")
dependentRate = float(numDependents) * 0.025
dependentDeductions = dependentRate * float(salary)
totalWithholding = stateTax + federalTax + dependentDeductions
takeHomePay = float(salary) - totalWithholding
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeductions))
print("Salary: $" + str(salary))
print("Take-Home Pay: $" + str(takeHomePay))
