# Calculatre injector parameters based upon what is found in the nasa document
import numpy as np
import restart as r
import excel as e
pi = np.pi
oholes = None
fholes = None


def run():
    print("\nWelcome to the NASA Injector Calculator!")
    print("Here you can find mass flow, the size of the injector outlets, accurate Chamber pressure (P1/Pc), the ratio between oxygen and fuel velocities, and the ratio between oxygen and fuel pressures\n")
    print("1: Metric 2: Imperial\n")
    units = input("What units do you use: ")
    if(units == '1'):
        print('metric')  # TODO
    elif(units == '2'):
        MdU = 'Lbm/sec'
        go = 32.2
        print('imperial\n')  # TODO
    else:
        units = input("Invalid input:")

    print('Recommendations/Equation Requirements: \nImpingement angle of 60 degrees\n0.79 ratio between ID/OD of outlets (uneven triplets)')

    print('\nFor this, first we will determine total mass flow (mdot)')
    F = float(input('F (Thrust): '))
    Is = float(input('Isp (specific impulse): '))
    if(units == '1'):
        mdot = F/(go*Is)
    if(units == '2'):
        mdot = F/Is
    print('\nmdot = ' + str(mdot) + ' ' + MdU)

    print('\nNext, how many elements and what type of injector are you making?')
    ele = input('Elements: ')
    print('\n1. Uneven Doublets\n2. Uneven Triplets')
    inj = input('\nInjector Type: ')
    global oholes
    global fholes
    oholes = int(ele)
    fholes = int(ele)

    def holeamt():
        global fholes
        global oholes
        fodouble = input('Will the oxidizer or fuel holes be doubled? f/o: ')
        if fodouble == 'f':
            fholes = int(ele) * 2
        elif fodouble == 'o':
            oholes = int(ele) * 2
        else:
            holeamt()
    if inj == '2':
        itype = 'Uneven Triplets'
        holeamt()
    else:
        itype = 'Uneven Doublets'
    print('oholes: ' + str(oholes))
    print('fholes: ' + str(fholes))

    print('\nNext, we will determine the area and therefore diameter of the injector outlets, starting with the oxidizer')
    Cd = float(input('Cd (density coefficient, recommended 0.6): '))
    pgo = float(input('p of the oxidizer: '))
    deltap = float(input('delta-p across injector (recommended 70 psi): '))
    TOA = mdot/(Cd*np.sqrt(2*go*pgo*deltap))
    print('\nTotal Oxidizer hole area: ' + str(TOA))
    IOA = TOA / oholes
    print('IOA: ' + str(IOA))

    print('\nNext, fuel hole')
    pgf = float(input('p of the fuel: '))
    TFA = mdot/(Cd*np.sqrt(2*go*pgf*deltap))
    print('Total Fuel hole area: ' + str(TFA))
    IFA = TFA / fholes
    print('IFA: ' + str(IFA))

    do = 2*np.sqrt(IOA/pi)
    df = 2*np.sqrt(IFA/pi)
    print('\nThe diameter of each oxidizer hole is ' + str(do) +
          ' in\nand the diameter of each fuel hole is ' + str(df) + ' in')

    print('\nNext, we will solve for chamber pressure, we will need c*, At and mdot for this')
    cstar = float(input('c* (effective exhaust velocity): '))
    At = float(input('At (throat area): '))
    if(units == '1'):
        c = cstar*mdot
        print('mdot')
    else:
        c = cstar*mdot
        print('mdot')
    P1 = c/At
    print('Chamber pressure: ' + str(P1))  # TODO fix this

    def extra():
        # TODO check necessity of this
        print('\nNext, we solve for the ratio of velocities')
        print('For this we need prefered k\', as the rest of the values were found above')
        k = float(input('prefered k\'(recommended 0.625): '))

        rf = df/2  # radius of fuel outlet
        ro = do/2  # radius of oxidizer outlet
        af = pi*rf*rf  # cross sectional area of fuel outlet
        ao = pi*ro*ro  # cross sectional area of oxidizer outlet
        c1 = np.power(2*ao/af, 0.25)  # part of formula
        v1_v2 = np.sqrt(k/(c1*pgo)*pgf)  # velocity ratios
        print('\nv1/v2 ratio:')
        print(v1_v2)

        # may not need this either
        print('\nAfter that, we solve Bernoulli\'s equation for the estimated pressures')
        print('THIS IS CURRENTLY INACCURATE AND NOT USEFUL')
        # deltay = input('Enter vertical distance between valves and the injector outlets:\n') may not need
        Po_Pf = ((pgo*v1_v2*v1_v2)/pgf)+(pgo/pgf)-1
        print(Po_Pf)

    con = input(
        '\nAFTER THIS POINT EQUATIONS ARE MOST LIKELY NOT NECESSARY, WOULD YOU LIKE TO CONTINE? y/n ')

    if con == 'y':
        extra()
    else:
        variables = [F, Is, mdot, ele, itype, oholes, fholes, Cd,
                     pgo, deltap, TOA, IOA, pgf, TFA, IFA, do, df]
        names = ['F (thrust)', 'Is (Specific Impulse', 'mdot (Mass Flow Rate)', 'Element Count', 'Injector Type', 'Oxidizer Holes', 'Fuel Holes', 'Cd (Density Coefficient)', 'p_o (Oxidizer Density)', 'delatp (Pressure Change over Injecor)',
                 'TOA (Total Oxidizer Hole Area)', 'IOA (Individual Oxidizer Hole Area)', 'p_f (Fuel Density)', 'TFA (Total Fuel Hole Area)', 'IFA (Individual Fuel Hole Area)', 'Do (Individual Oxidizer Hole Diameter', 'Df (Individual Fuel Hole Diameter']
        equations = e.pretty(['Predetermined', 'Propellant Info', 'mdot = F/Is', 'Predetermined Estimate', 'Predetermined', 'Predetermined Estimate', 'Predetermined Estimate', 'Predetermined Estimate', 'Propellant Info', 'Predetermined Estimate',
                              'TOA = mdot/(Cd*np.sqrt(2*go*pgo*deltap))', 'IOA = TOA / o-hole-count', 'Propellant Info', 'TFA = mdot/(Cd*np.sqrt(2*go*pgf*deltap))', 'IFA = TFA / f-hole-count', 'Do = 2*np.sqrt(IOA/pi)', 'Df = 2*np.sqrt(IFA/pi)'])

        sheet = input('Would you like a excel spreadsheet? y/n ')
        if sheet == 'y':
            e.sheet(variables, names, equations, 'Injector')

        r.restart()
