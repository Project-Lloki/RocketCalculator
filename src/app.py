import cc as c1
import injector as c2
import tanks as c3
import thrustFile as c5
import units as u

unstarted = True


def run():
    global unstarted

    print('\nWelcome to the RocketCalculator!\n')

    u.init()

    print('1: Combustion Chamber \n2: Injector Design \n3: Tanks\n4: Apogee Optimization \n5: Thrust File')
    calculator = input('\nChoose your calculator: ')

    if calculator == '1':
        c1.run()
    elif calculator == '2':
        c2.run()
    elif calculator == '3':
        c3.run()
    elif calculator == '5':
        c5.run()
    else:
        print('choose a proper calculator')


run()
