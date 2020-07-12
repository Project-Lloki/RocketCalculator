#Run file for all of the calculators
import cc as c1
import injector_nasa as c2

print('\nWelcome to the RocketCalculator!\n')
print('1: Combustion Chamber \n2: Injector Design \n3: Appogee\n')
calculator = input('Choose your calculator: \n')

if calculator == 1: #make sure to change back to string
    c1.run()
elif calculator == 2: #make sure to change back to string
    c2.run()
else :
    calculator = input('Choose a proper calculator: \n')

