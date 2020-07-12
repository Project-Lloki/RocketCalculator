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

    print('\nNext, we solve for the ratio of velocities') #TODO check necessity of this
    print('\nFor this, we will need p (specific gravity) of the oxidizer and fuel, A (cross sectional area) of the fuel and oxidizer holes, and prefered k\'')
    pgf = input('\np of the fuel:\n') 
    pgo = input('p of the oxidizer:\n')
    df = input('diameter of the fuel outlet:\n') #TODO automate through ratios
    do = input('diameter of the oxidizer outlet:\n')
    k = input('prefered k\'(recommended 0.625):\n')

    rf = df/2 #radius of fuel outlet
    ro = do/2 #radius of oxidizer outlet
    af = pi*rf*rf #cross sectional area of fuel outlet
    ao = pi*ro*ro #cross sectional area of oxidizer outlet
    c1 = np.power(2*ao/af, 0.25) #part of formula
    v1_v2 = np.sqrt(k/(c1*pgo)*pgf) #velocity ratios
    print('\nv1/v2 ratio:')
    print(v1_v2)

    print('\nAfter that, we solve Bernoulli\'s equation for the estimated pressures') #may not need this either
    





    