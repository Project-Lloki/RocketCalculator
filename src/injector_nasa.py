#Calculatre injector parameters based upon what is found in the nasa document
import numpy as np
pi = np.pi

def run():
    print("\nWelcome to the NASA Injector Calculator! \n")
    print("Here you can find TODO\n")
    print("1: Metric 2: Imperial\n")
    units = input("What units do you use:\n")
    if(units == 1):
        print('metric') #TODO
    elif(units == 2):
        print('imperial') #TODO
    else: units = input("Invalid input:")

    print('\nFirst, we will solve for chamber pressure, we will need c*, At and mdot for this')
    cstar = input('\nc* (effective exhaust velocity):')
    At = input('\nAt (throat area):')
    mdot = input('\nmdot (total mass flow):') #TODO add a mdot calculator before this
    c = cstar*mdot
    P1 = float(c)/At
    print(P1)

    print('\nNext, we solve Bernouli\'s equation for the ratio of velocities') #TODO check necessity of this
    print('\nFor this, we will need p (specific gravity) of the oxidizer and fuel, A (cross sectional area) of the fuel and oxidizer holes, and prefered k\'')
    #pgf = input('\np of the fuel:') may not be needed
    pgo = input('\np of the oxidizer:')
    df = input('\ndiameter of the fuel outlet:') #TODO automate through ratios
    do = input('\ndiameter of the oxidizer outlet:')
    k = input('\nprefered k\'(recommended 0.625):')

    print('it is understood that v2 = 0, due to the liquids starting from rest at the valves')
    rf = df/2
    ro = do/2
    af = pi*rf*rf
    ao = pi*ro*ro
    c1 = np.power(2*ao/af, 0.25)
    v1 = np.sqrt(k/(c1*pgo))
    print(v1)





    