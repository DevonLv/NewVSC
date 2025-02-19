#Generate and Printe Employee's Bonus based on Productivity Bonus
#User Inputs for Employee Name, Shifts and Transactions
Fname=input("Enter First Name of Employee: ")
Lname=input("Enter Last Name of Employee: ")
empName=Fname + " " + Lname
numShifts=int(input("Enter the number of shifts: "))
numTrans=int(input("Enter the number of transactions: "))
transDollars=float(input("Enter the total dollar amount of transactions: "))

#Calculate Employee's Productivity Score
transAvg=int(transDollars/numTrans)
prodScore=transAvg/numShifts

#Calculate Employee's Bonus
empBonus=0
if prodScore<=30:
    empBonus=50.00
elif prodScore>= 31 and prodScore<= 69:
    empBonus=75.00
elif prodScore>= 70 and prodScore<= 199:
    empBonus=100.00
elif prodScore>= 200:
    empBonus=200.00

#Display Employee's Name and Bonus
print(f"Employee's Name: " + empName)
print(f'Bonus: ${empBonus}')