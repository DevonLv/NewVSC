testScore=int(input("Enter your test score: "))
classRank=int(input("Enter your class rank: "))
if testScore>=90:
    if classRank>=25:
        print("Accept")
    else:
        print("Reject")
elif testScore>=80:
    if classRank>=50:
        print("Accept")
    else:
        print("Reject")
elif testScore>=70:
    if classRank>=75:
        print("Accept")
    else:
        print("Reject")
else:
    print("Reject")