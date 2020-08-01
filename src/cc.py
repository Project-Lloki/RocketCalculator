#Calculate combustion chamber parameters, with values given
# F = Cf*Pc*At
import restart as r
import numpy as np
import sympy as sym

def run():
    print("\nWelcome to the Combustion Chamber Calculator! \n")
    print("Here you can find thrust (F), coefficient of thrust (Cf), Chamber Pressure (Pc) or Throat Area (At) when you know at least three of these values.\n")
    print("1: Metric 2: Imperial\n")
    units = input("What units do you use: ")
    if(units == '1'):
        FU = 'N' 
        PU = ''
        AU = ''
        g = 9.81
    elif(units == '2'):
        FU = 'Lbf' 
        PU = 'psi' 
        AU = 'in^2'
        g = 32.2
    else: units = input("Invalid input:")

    print("\nChoose the value you wish to calculate for:")
    print("\n 1: F (thrust) \n 2: Cf (Coefficient of thrust) \n 3: Pc (Chamber Pressure) \n 4: At (Throat area)\n")
    solve = input("What are you solving for? ")

    def thrust():
        Cf = float(input("Cf:"))
        Pc = float(input("Pc (" + PU + "):"))
        At = float(input("At(" + AU + "):"))
        F = Cf*Pc*At
        return F

    def coefficient():
        F = float(input("F(" + FU + "):"))
        Pc = float(input("Pc (" + PU + "):"))
        At = float(input("At(" + AU + "):"))
        k = Pc*At
        Cf = F/k
        return Cf

    def pressure():
        F = float(input("F(" + FU + "):"))
        Cf = float(input("Cf:"))
        At = float(input("At(" + AU + "):"))
        k = Cf*At
        Pc = F/k
        return Pc

    def throat():
        F = float(input("F(" + FU + "):"))
        Cf = float(input("Cf:"))
        Pc = float(input("Pc (" + PU + "):"))
        k = Cf*Pc
        At = F/k
        return At

    if(solve == 1):
        print(thrust())
    elif(solve == 2):
        print(coefficient())
    elif(solve == 3):
        print(pressure())
    elif(solve == 4):
        print(throat())

    print('\nNext, we will solve for chamber pressure, we will need c*, At and mdot for this')
    cstar = float(input('c* (effective exhaust velocity): '))
    At = float(input('At (throat area): '))
    # if(units == '1'):
    #     c = cstar*mdot
    #     print('mdot')
    # else: 
    #     c = cstar*imdot
    #     print('imdot')
    Pc = cstar/At
    print('Chamber pressure: ' + str(Pc)) #TODO fix this
    
    print('We will now find exit velocity.')
    Mo = float(input('Molecular weight of combustion products: '))
    y = float(input('Specific heat ratio (Cp/Cv), 1.24: '))
    R = (1544/Mo) #Gas Constant (ft/deg R) 
    Tc = float(input('Temperature of combustion: '))
    #Mi = input('Mach number at nozzle inlet (usually range between 0.15 and 0.45): ') #equation: vi/ai (flow velocity/velocity of sound)
    #Tc = Ti*(1+(0.5*(y-1))*Mi) #Nozzle stagnation temperature  
    #Pe = float(input('Flow static pressure at exit: ')) #Flow static pressure at exit #TODO find equation
    #Ve = V, Tc = T, R = R, Pe = E, Pc = C, y=y
    #Ve = np.sqrt(((2*g*y)/y-1)*R*Tc*(1-(Pe/Pc)**((y-1)/y))) 
    V, T, R, E, C, y, g = sym.symbols('V T R E C y g')
    expr = sym.sqrt(((2*g*y)/y-1)*R*C*(1-(E/C)**((y-1)/y))) 
    print('expr: ' + str(expr))
    print(sym.solve(E))
    # print('Ve: ' + str(Ve))
    #E = [(C**(-1/y)*(2*C*R*g - C*R - V**2)/(R*(2*g - 1)))**(y/(y - 1))]

    print('Next, Gas Weight Flow Rate')
    Wdot = At*Pc*np.sqrt((g*y*(2/(y+1))**(y+1)/(y-1))/(R*Tc))
    print('Wdot: ' + str(Wdot))

    print('Next, Nozzle Exit Area and Nozzle Expansion Ratio')
    At = (((y+1)/(y-1))*(1-(Pe/Pc)^((y-1)/y)))^(1/2)
    Ae = ((2/(y+1))**1/(y-1))*((Pc/Pe)**(1/y)) #Area of nozzle exit
    E = Ae/At #Expansion Ratio
    print('Ae: ' + str(Ae))
    print('Fancy E: ' + str(E))

    print('Next, pressure at the throat')
    Pt = pc*((2/(y+1))**(y/(y-1))) #Throat Pressure
    print('Pt: ' + str(Pt))

    print('Next, flow velocity at the throat')
    Vt = np.sqrt(((2*g*y)/(y+1)*R*Tc)) #Flow veolcity at throat
    print('Vt: ' + str(Vt))

    print('Next, Area at any point between the nozzle inlet and nozzle exit') #TODO make a graph or equation in order to easily model
    Mx = input() #Mach number at X TODO find equaiton
    Ax1 = (At/Mx)*np.sqrt(((1+((y-1)/2)*Mx)/(y+1)/2)**((y+1)/(y-1)))
    print('Ax1: ' + str(Ax1))

    print('Next, Area at any point between the nozzle inlet and nozzle throat') #TODO make a graph or equation in order to easily model
    Px = input() #Pressure at X TODO find equation
    Ax2 = At*((((2/(y+1))*(Pc/Px)**((y-1)/y))**((y+1)/(2*(y-1)))))/np.sqrt((2/(y-1))*((Pc/Px)**((y-1)/y)-1))
    print('Ax2: ' + str(Ax2))

    print('Next, Area at any point between the nozzle throat and nozzle exit') #TODO make a graph or equation in order to easily model
    Px1 = input() #Pressure at X TODO find equation
    Ax3 = At*((((2/(y+1))*(Pc/Px)**(1/y)))/np.sqrt(((y+1)/(y-1))*(1-(Px/Pc)**((y-1)/y))))
    print('Ax3: ' + str(Ax3))

    print('Next, velocity at any point between nozzle throat and nozzle exit')
    Vx = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Px/Pc)**((y-1)/y))) #Flow velocity at X
    print('Vx: ' + str(Vx))


    r.restart()

