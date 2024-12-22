def main():
    
    #set empty list to be appended to and placeholder check for while loop
    userList = []
    cStopList = 0
    while cStopList != 'n': #while loop to append values to list, checks for Y or N input
        
        userList.append(getFloatInput('Enter property sales value: '))
        cStopList = get_y_n('Enter another value? Y or N: ')

    #sorting list and setting a count variable
    userList.sort()
    count = 0
    
    for x in userList:  #prints each property number and value from least to greatest
        print(f'Property {count + 1} {"$":5}{userList[count]:.2f}') 
        count += 1
    
    print(f'{"Minimum:":13}{"$":5}{min(userList):,.2f}')
    print(f'{"Maximum:":13}{"$":5}{max(userList):,.2f}')
    print(f'{"Total:":13}{"$":5}{sum(userList):,.2f}')
    print(f'{"Average:":13}{"$":5}{sum(userList) / len(userList):,.2f}')
    print(f'{"Median:":13}{"$":5}{getMedian(userList):,.2f}')
    print(f'{"Commission:":13}{"$":5}{(sum(userList) * .03):,.2f}')


    return


def getFloatInput(sPrompt): #data validation for property values
    
    while True:
        try:
            value = float(input(sPrompt))
            if value > 0:
                break  # exit if input is greater than 0
            else:
                print("Input must be a number Greater than 0")

        except ValueError:  # checks for a value error
            print("Input must be a number Greater than 0")

    return value

def get_y_n(prompt):    #data validation for Y or N
    
    while True:
        value = input(prompt).lower()
        if value == 'y' or value == 'n':
            break  
        else:
            print("Enter another value Y or N: ")
    
    return value

def getMedian(list):    #gets median value for user list
    
    listLength = len(list)
    
    if listLength % 2 == 0: #even list len. 
        median = (list[listLength // 2] + list[listLength // 2 - 1]) / 2
        
    else: #odd list len.
        median = list[listLength // 2]

    return median

main()
