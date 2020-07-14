#Calculatre injector parameters based upon what is found in the nasa document
import numpy as np
pi = np.pi

def run():
    print("\nWelcome to the NASA Injector Calculator! \n")
    print("Here you can find mass flow, accurate Chamber pressure (P1/Pc), the ratio between oxygen and fuel velocities, and the ratio between oxygen and fuel pressures\n")
    print("1: Metric 2: Imperial\n")
    units = input("What units do you use:\n")
    if(units == '1'):
        print('metric') #TODO
    elif(units == '2'):
        print('imperial') #TODO
    else: units = input("Invalid input:")

    print('Recommendations/Equation Requirements: \nImpingement angle of 60 degrees\n0.79 ratio between ID/OD of outlets (uneven triplets)')

    print('First, we will determine total mass flow (mdot)')
    F = float(input('\nF (thrust): '))
    if(units == '2'):
        F = F * 4.44822
    go = 9.82
    igo = 32.2
    Is = float(input('\nIsp (specific impulse): '))
    mdot = F/(go*Is)
    print('mdot = ' + str(mdot) + ' kg/s')
    imdot = mdot * 2.204623
    print('mdot = ' + str(imdot) + ' lb/s')

    print('Next, we will determine the area and therefore diameter of the injector outlets, starting with the oxidizer')
    Cd = float(input('\nCd (density coefficient, recommended 0.6): '))
    pgo = float(input('\np of the oxidizer: '))
    deltap = float(input('\ndelat-p across injector (recommended 70 psi):'))
    Aho = imdot/(Cd*np.sqrt(igo*pgo*deltap))
    print('\nOxidizer hole area: ' + str(Aho))

    print('\nNext, fuel hole')
    pgf = float(input('\np of the fuel: '))
    Ahf = imdot/(Cd*np.sqrt(igo*pgf*deltap))
    print('\nFuel hole area: ' + str(Ahf))

    do = 2*np.sqrt(Aho/pi)
    df = 2*np.sqrt(Ahf/pi)
    print('\nTherefore, the diameter of the oxidizer hole is ' + str(do) + ' in\nand the diameter of the fuel hole is ' + str(df) + ' in')


    print('\nNext, we will solve for chamber pressure, we will need c*, At and mdot for this')
    cstar = float(input('\nc* (effective exhaust velocity): '))
    At = float(input('\nAt (throat area): '))
    if(units == 1):
        c = cstar*mdot
    else: c = cstar*imdot
    P1 = c/At
    print(P1)

    print('\nNext, we solve for the ratio of velocities') #TODO check necessity of this
    print('\nFor this, we will need p (specific gravity) of the oxidizer and fuel, A (cross sectional area) of the fuel and oxidizer holes, and prefered k\'')
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

    back = input('\nWould you like to go to another calculator? y/n \n')
    if back == 'y':
        import app
        app.run()
    elif back == 'n':
        print('OK!')
    else:
        back = input('\nInvalid input! Would you like to go to another calculator? y/n \n')
    
    





    