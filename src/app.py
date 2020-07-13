#Run file for all of the calculators
import cc as c1
import injector_nasa as c2
import tanks as c3

def run():
    print('\nWelcome to the RocketCalculator!\n')
    print('1: Combustion Chamber \n2: Injector Design \n3: Tanks\n')
    calculator = input('Choose your calculator: \n')

    if calculator == '1':
        c1.run()
    elif calculator == '2':
        c2.run()
    elif calculator == '3':
        c3.run()
    else:
        print('choose a proper calculator')

run()