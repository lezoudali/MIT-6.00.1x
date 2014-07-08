"""
write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month
"""

balance = 3329
annualInterestRate = 0.2

first = balance
monthlyInterestRate = annualInterestRate/12

minPayment = 10

i = 1
while balance >0:
    balance -= minPayment
    balance = (balance * (1 + monthlyInterestRate))
    i += 1 
    if i == 13 and balance >0:
        minPayment +=10
        balance = first
        i = 1
print "Lowest Payment: " + str(minPayment)