import math

def main():
    #getting user input with data val. function
    fWallSqFeet = float(getFloatInput("Enter wall space in square feet: "))
    fPaintPrice = float(getFloatInput("Enter paint price per gallon: "))
    fFeetPerGal = float(getFloatInput("Enter feet per gallon: "))
    fLaborHrGal = float(getFloatInput("How many labor hours per gallon?: "))
    fPaintLaborHourly = float(getFloatInput("Labor Charge per hour: "))
    sGetState = (input('State job is in: ')).lower()
    sLastName = (input('Customer Last Name: '))

    #calculations
    iGallonsPaint = getGallonsOfPaint(fWallSqFeet, fFeetPerGal)
    fLaborHrs = getLaborHours(fLaborHrGal, iGallonsPaint)
    fPaintCharge = getPaintCost(iGallonsPaint, fPaintPrice)
    fLaborCharge = getLaborCost(fLaborHrs, fPaintLaborHourly)
    fTax = getSalesTax(sGetState) * (fLaborCharge + fPaintCharge)
    fTotal = fPaintCharge + fLaborCharge + fTax
    
    
    print(f'Gallons of paint: {iGallonsPaint}')
    print(f'Hours of labor: {fLaborHrs}')
    #calls function that prints calculations
    showCostEstimate(fPaintCharge,fLaborCharge,fTax,fTotal)
    
    #sets file name
    #writes each line with a calcuated value
    fileName = sLastName + '_PaintJobOutput'
    with open(f'{fileName}.txt','w') as ofPaintJobOutput:
        ofPaintJobOutput.write(f'Gallons of paint: {iGallonsPaint}\n')
        ofPaintJobOutput.write(f'Hours of labor: {fLaborHrs}\n')
        ofPaintJobOutput.write(f'Paint Charges: ${fPaintCharge:,.2f}\n')
        ofPaintJobOutput.write(f'Labor Charges: ${fLaborCharge:,.2f}\n')
        ofPaintJobOutput.write(f'Tax: ${fTax:,.2f}\n')
        ofPaintJobOutput.write(f'Total cost: ${fTotal:,.2f}')
    
    print(f'File: {fileName}.txt was created.')


#data validation
def getFloatInput(fPrompt):

    while True:
        try:
            value = float(input(fPrompt))
            if value >= 0:
                break  # exit if input is greater than 0
            else:
                print("Input must be a positive numeric value")

        except ValueError:  # checks for a value error
            print("Input must be a positive numeric value")

    return value


def getSalesTax(state):
    #tuples for constant states and tax rates
    STATES = ("ct", "ma", "me", "nh", "ri", "vt")
    RATES = (.06, .0625, .085, .0, .07, .06)
    
    #checks if inputted state is in state tuple
    if state in STATES:
        i = STATES.index(state) #if input is found gets the index of tuple
        tax = RATES[i] #takes the stored index from above and stores corresponding value from Rates tuple
    else:
        tax = 0 #if input is not found tax rate is 0

    return tax


def getGallonsOfPaint(wallSqFt, feetPerGal):
#wall sq feet / feet per gal. rounds up to next int
    gallons = wallSqFt / feetPerGal 
    iGallonsRound = math.ceil(gallons)

    return iGallonsRound


def getLaborHours(laborHoursGal, totalGal):
#time to complete work. hours per gal * total gal
    fLaborHours = laborHoursGal * totalGal
    
    return fLaborHours


def getLaborCost(laborHoursGal, paintLaborHourly):
#labor cost. hours * hourly pay
    fLaborCost = laborHoursGal * paintLaborHourly

    return fLaborCost


def getPaintCost(totalGal, paintPrice):
#price of paint * gals of paint
    fPaintCost = totalGal * paintPrice

    return fPaintCost


def showCostEstimate(fPaintCharge,fLaborCharge,fTax,fTotal):
    #prints the totals
    print(f'Paint Charges: ${fPaintCharge:,.2f}')
    print(f'Labor Charges: ${fLaborCharge:,.2f}')
    print(f'Tax: ${fTax:,.2f}')
    print(f'Total cost: ${fTotal:,.2f}')


main()

