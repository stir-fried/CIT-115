#asking for inputs
strName = input('Name of person that we are calculating the grades for: ')
iTest1 = int(input('Test 1: '))
iTest2 = int(input('Test 2: '))
iTest3 = int(input('Test 3: '))
iTest4 = int(input('Test 4: '))
cDropLowest = input('Do you wish to Drop the Lowest Grade? ')    
    
# checking for negatives
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0 :
    print('Test scores must be greater than 0')
    raise SystemExit

#checking if grade will be dropped and calculating
if cDropLowest == 'n'  or cDropLowest == 'N' :
    fAvgGrade = (iTest1 + iTest2 + iTest3 + iTest4) / 4
    print(f'{strName} test average is: {fAvgGrade:.1f}')
elif cDropLowest == 'y' or cDropLowest == 'Y':
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fAvgGrade = (iTest2 + iTest3 + iTest4) / 3
        print(f'{strName} test average is: {fAvgGrade:.1f}')
    elif iTest2 <= iTest3 and iTest2 <= iTest4  :
        fAvgGrade = (iTest1 + iTest3 + iTest4) / 3
        print(f'{strName} test average is: {fAvgGrade:.1f}')
    elif iTest3 <= iTest4 :
        fAvgGrade = (iTest1 + iTest2 + iTest4) / 3
        print(f'{strName} test average is: {fAvgGrade:.1f}')
    else:
        fAvgGrade = (iTest1 + iTest2 + iTest3) / 3
        print(f'{strName} test average is: {fAvgGrade:.1f}')
else:
    print('Enter Y or N to Drop the Lowest Grade.')
    raise SystemExit

#checking letter grade
if fAvgGrade >= 97.0 :
    sletterGrade = 'A+'
elif fAvgGrade >= 94.0 :
    sletterGrade = 'A'
elif fAvgGrade >= 90.0 :
    sletterGrade = 'A-'
elif fAvgGrade >= 87.0 :
    sletterGrade = 'B+'
elif fAvgGrade >= 84.0 :
    sletterGrade = 'B'
elif fAvgGrade >= 80.0 :
    sletterGrade = 'B-'
elif fAvgGrade >= 77.0 :
    sletterGrade = 'C+'
elif fAvgGrade >= 74.0 :
    sletterGrade = 'C'
elif fAvgGrade >= 70.0 :
    sletterGrade = 'C-'
elif fAvgGrade >= 67.0 :
    sletterGrade = 'D+'
elif fAvgGrade >= 64.0 :
    sletterGrade = 'D'
elif fAvgGrade >= 60.0 :
    sletterGrade = 'D-'
else:
    sletterGrade = 'F'

print(f'Letter Grade for the test is: {sletterGrade}')
