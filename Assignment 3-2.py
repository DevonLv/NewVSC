test_score=int(input("Enter your test score: "))
class_rank=int(input("Enter your class rank: "))
if test_score>=90:
    if class_rank>=25:
        print("Accept")
    else:
        print("Reject")
elif test_score>=80:
    if class_rank>=50:
        print("Accept")
    else:
        print("Reject")
elif test_score>=70:
    if class_rank>=75:
        print("Accept")
    else:
        print("Reject")
else:
    print("Reject")