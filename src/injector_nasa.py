#Calculatre injector parameters based upon what is found in the nasa document
import numpy as np
import restart as r
pi = np.pi
oholes = None
fholes = None

def run():
    print("\nWelcome to the NASA Injector Calculator!")
    print("Here you can find mass flow, the size of the injector outlets, accurate Chamber pressure (P1/Pc), the ratio between oxygen and fuel velocities, and the ratio between oxygen and fuel pressures\n")
    print("1: Metric 2: Imperial\n")
    units = input("What units do you use: ")
    if(units == '1'):
        print('metric') #TODO
    elif(units == '2'):
        print('imperial\n') #TODO
    else: units = input("Invalid input:")

    print('Recommendations/Equation Requirements: \nImpingement angle of 60 degrees\n0.79 ratio between ID/OD of outlets (uneven triplets)')

    print('\nFirst, we will determine total mass flow (mdot)')
    F = float(input('F (thrust): '))
    if(units == '2'):
        F = F * 4.44822
    go = 9.82
    igo = 32.2
    Is = float(input('Isp (specific impulse): '))
    mdot = F/(go*Is)
    print('\nmdot = ' + str(mdot) + ' kg/s')
    imdot = mdot * 2.204623
    print('mdot = ' + str(imdot) + ' lb/s')

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
        else: holeamt()
    if inj == '2': 
        holeamt()
    print('oholes: ' + str(oholes))
    print('fholes: ' + str(fholes))
   
    print('\nNext, we will determine the area and therefore diameter of the injector outlets, starting with the oxidizer')
    Cd = float(input('Cd (density coefficient, recommended 0.6): '))
    pgo = float(input('p of the oxidizer: '))
    deltap = float(input('delta-p across injector (recommended 70 psi): '))
    Aho = imdot/(Cd*np.sqrt(2*igo*pgo*deltap))
    print('\nTotal Oxidizer hole area: ' + str(Aho))
    oArea = Aho / oholes
    print('oArea: ' + str(oArea))

    print('\nNext, fuel hole')
    pgf = float(input('p of the fuel: '))
    Ahf = imdot/(Cd*np.sqrt(2*igo*pgf*deltap))
    print('Total Fuel hole area: ' + str(Ahf))
    fArea = Ahf / fholes
    print('fArea: ' + str(fArea))

    do = 2*np.sqrt(oArea/pi)
    df = 2*np.sqrt(fArea/pi)
    print('\nThe diameter of each oxidizer hole is ' + str(do) + ' in\nand the diameter of each fuel hole is ' + str(df) + ' in') 

    print('\nNext, we will solve for chamber pressure, we will need c*, At and mdot for this')
    cstar = float(input('c* (effective exhaust velocity): '))
    At = float(input('At (throat area): '))
    if(units == '1'):
        c = cstar*mdot
        print('mdot')
    else: 
        c = cstar*imdot
        print('imdot')
    P1 = c/At
    print('Chamber pressure: ' + str(P1)) #TODO fix this

    def extra():
        print('\nNext, we solve for the ratio of velocities') #TODO check necessity of this
        print('For this we need prefered k\', as the rest of the values were found above')
        k = float(input('prefered k\'(recommended 0.625): '))

        rf = df/2 #radius of fuel outlet
        ro = do/2 #radius of oxidizer outlet
        af = pi*rf*rf #cross sectional area of fuel outlet
        ao = pi*ro*ro #cross sectional area of oxidizer outlet
        c1 = np.power(2*ao/af, 0.25) #part of formula
        v1_v2 = np.sqrt(k/(c1*pgo)*pgf) #velocity ratios
        print('\nv1/v2 ratio:')
        print(v1_v2)

        print('\nAfter that, we solve Bernoulli\'s equation for the estimated pressures') #may not need this either
        print('THIS IS CURRENTLY INACCURATE AND NOT USEFUL')
        #deltay = input('Enter vertical distance between valves and the injector outlets:\n') may not need
        Po_Pf = ((pgo*v1_v2*v1_v2)/pgf)+(pgo/pgf)-1
        print(Po_Pf)

    con = input('\nAFTER THIS POINT EQUATIONS ARE MOST LIKELY NOT NECESSARY, WOULD YOU LIKE TO CONTINE? y/n ')

    if con == 'y':
        extra()
    else: 
        r.restart()