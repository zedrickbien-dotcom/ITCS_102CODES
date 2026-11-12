

loan = float(input("enter loan"))
years = int(input("Enter years to pay"))
monthly = years * 12
principal = loan/monthly
remaining_bal = loan
print("|\tmonthly\t|\tpayment\t|\tinterest\t|\tprincipal\t|\tbalance\t|")
for count in range(1,monthly + 1):
    remaining_bal -= principal
    interest = remaining_bal = 0.00256
    pay = interest + principal
    print(f"|{count}\t|\t{round(pay,2)}\t\t|\t{round(interest, 2)}\t\t|\t{round(principal, 2)}\t|\t{round(remaining_bal, 2)}\t|")