"""
Write a program that uses bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.

"""

balance = 320000
annualInterestRate = 0.2

first = balance
monthlyInterestRate = annualInterestRate/12

lower = balance/12
upper = (balance * ((1 + monthlyInterestRate)**12)) / 12.0

minPayment = (lower + upper)/2.0

i = 0

while i < 12:
    balance -= minPayment
    balance = (balance * (1 + monthlyInterestRate))
    i += 1
    if i == 12 and round(balance) > 0:
        lower = minPayment
        minPayment = (lower + upper )/2.0
        balance = first
        i = 0
    elif i == 12 and round(balance) < 0:
        upper = minPayment
        minPayment = (lower + upper )/2.0
        balance = first
        i = 0

print "Lowest Payment: %.2f " % (minPayment)
