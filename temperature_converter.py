#Greeting
print("Javier's Temp converter: ")

#ask for temperature and unit of measurements
fTemperature = float(input('Enter a temperature: '))
cUnit = input('Is the temp F for Fahrenheit or C for Celcius? ')

#converts F to C
def fnFahrenheitToCelsius():
    if fTemperature > 212 :
        print('Temp can not be > 212')
    else:
        print(f'The Celsius equivalent is: {(5/9)*(fTemperature - 32):.1f}')
               
#converts C to F
def fnCelsiusToFahrenheit():
    if fTemperature > 100 :
        print('Temp can not be > 100')
    else:
        print(f'The Fahrenheit equivalent is: {((9/5)*fTemperature)+ 32:.1f}')
        
#checks if user entered an f or c 
if cUnit == 'f' or cUnit == 'F':
    fnFahrenheitToCelsius()
elif cUnit == 'c' or cUnit == 'C':
    fnCelsiusToFahrenheit()
else:
    print('You must enter a F or C')
   

   #sdjhfbjkada;fd