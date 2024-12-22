# asking user for values
nPrincipalInvestment = float(input("Enter the starting principal: "))
nInterestRate = float(input("Enter the annual interest rate: "))
nCompounding = float(input("How many times per year is the interest compounded? "))
nPeriods = float(input("For how many years will the account earn interest? "))

# converting interest rate to perecentage
nInterestRate = nInterestRate / 100

# calculating future value fv=(1+r/m)**(m*t)
nFutureValue = (((nInterestRate / nCompounding) + 1) ** (nCompounding * nPeriods)) * nPrincipalInvestment

# printing future value after X years
print(f"At the end of {int(nPeriods)} years you will have $ {nFutureValue:,.2f}")
