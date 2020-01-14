#TIP CALCULATOR
level_of_service = ("good", "fair", "bad")

bill_amount = int(input("Enter total bill amount: "))
level_of_service = input("Enter level of service (good,fair or bad): ")
tip_amount = 0.0
if (level_of_service == "good"):
    tip_amount = bill_amount * .20
elif (level_of_service == "fair"):
    tip_amount = bill_amount * .15
elif(level_of_service == "bad"):
    tip_amount = bill_amount * .10
else:
    print("Please enter again.")
total_amount = tip_amount + bill_amount

print("%.2f" %  tip_amount)
print("%.2f" % total_amount)



