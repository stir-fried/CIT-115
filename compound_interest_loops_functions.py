#validation for values must be > 0
def GetInput(nPrompt):
    
    while True :
        try:
            value = float(input(nPrompt))
            if value > 0:
                break #exit if input is greater than 0
            else:
                print('Input must be a positive numeric value')

        except ValueError: #checks for a value error
            print('Input must be a positive numeric value')

    return value

#get input and validation for number that is >= 0
def GetInputGoal(GoalPrompt):
    
    while True:
        try:
            value = float(input('What is the Goal Amount (can enter 0 but not negative) '))
            if value >= 0:
                break #exit if input is 0 or greater
            else:
                print('Input must be 0 or greater')
        except ValueError: #checks for a value error
            print('Input must be a positive numeric value')
    
    return value

def GetMonthlyBalance(nDeposit, nInterest, nPeriods):
    
    for iCount in range(1,nPeriods+1):
        nDeposit = nDeposit + (nDeposit * nInterest)
        nMonthlyBalance = nDeposit
        print(f'Month: {iCount}  Account Balance is: $ {nMonthlyBalance:,.2f}')
    

def TimeToGoal(nDeposit, nInterest, nGoal):
    
    iMonths = 0
    nMonthlyBalance = nDeposit
    
    while nMonthlyBalance < nGoal:
        nDeposit = nDeposit + (nDeposit * nInterest)
        nMonthlyBalance = nDeposit
        iMonths += 1

    return iMonths


#get user input
fDeposit = float(GetInput("What is the Original Deposit (positive value) "))

fInterestRatePercentage = float(GetInput("What is the Interest Rate (positive value) "))

iPeriods = int(GetInput("What is the Number of Months (positive value) "))

fGoal = float(GetInputGoal('What is the Goal Amount (can enter 0 but not negative) '))

#convert rate to percentage and calculate monthly rate
fMonthlyInterestRate = (fInterestRatePercentage/100) / 12

GetMonthlyBalance(fDeposit,fMonthlyInterestRate,iPeriods)

print(f'It will take:  {TimeToGoal(fDeposit,fMonthlyInterestRate,fGoal)}  months to reach the goal of $ {fGoal:,.2f}')
