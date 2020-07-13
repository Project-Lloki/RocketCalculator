#Run file for all of the calculators
import cc as c1
import injector_nasa as c2

print('\nWelcome to the RocketCalculator!\n')
print('1: Combustion Chamber \n2: NASA Injector Design \n3: Appogee\n')
calculator = input('Choose your calculator: \n')

if calculator == '1': 
    c1.run()
elif calculator == '2': 
    c2.run()
else :
    calculator = input('Choose a proper calculator: \n')

