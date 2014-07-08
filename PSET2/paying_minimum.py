"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
"""

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12

totalPaid = 0
i = 1
while i < 13:
    monthly = (monthlyPaymentRate)*(balance)
    monthly = round(monthly, 2)
    totalPaid += monthly
    unpaid = balance - monthly
    unpaid = round(unpaid, 2)
    balance = unpaid + (unpaid*monthlyInterestRate)
    balance = round(balance, 2)
    print "Month: %d" % (i)
    print "Minimum monthly payment: %.2f" % (monthly)
    print "Remaining balance: %.2f" % (balance)
    
    i += 1
    
print "Total paid: %.2f" % (totalPaid)
print "Remaining balance: %.2f" % (balance)