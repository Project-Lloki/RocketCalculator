# Calculate combustion chamber parameters, with values given
# F = Cf*Pc*At
import restart as r
import numpy as np
import sympy as sym
import excel as e


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
        VU = 'ft/sec'
        MdU = 'Lbm/sec'
        TU = 'R°'
        g = 32.2
        DU = 'in'
    else:
        units = input("Invalid input:")

    pi = np.pi

    print("\nFirst, we solve for the Area of the Throat:")

    F = float(input("F (" + FU + "): "))
    Cf = float(input("Cf: "))
    Pc = float(input("Pc estimate (" + PU + "): "))
    At = F/(Cf*Pc)
    print("At: " + str(At) + ' ' + AU)

    print('\nFor this, first we will determine total mass flow (mdot)')
    Is = float(input('Isp (specific impulse): '))
    if(units == '1'):
        mdot = F/(go*Is)
    if(units == '2'):
        mdot = F/Is
    print('\nmdot = ' + str(mdot) + ' ' + MdU)

    print('\nWe will now find exit velocity.')
    Mo = float(input('Molecular weight of combustion products, 23.3M: '))
    y = float(input('Specific heat ratio (Cp/Cv), 1.24: '))
    R = (1544/Mo)  # Gas Constant (ft/deg R)
    Tc = float(input('Temperature of combustion (' + TU + '): '))

    # Pc = Pi[1+0.5(y-1)Mi]^y/y-1, Pi = Pinj[1+y*Mi^2]
    #Ve = np.sqrt(((2*g*y)/y-1)*R*Tc*(1-(Pe/Pc)**((y-1)/y)))
    #At = (((y+1)/(y-1))*(1-(Pe/Pc)**((y-1)/y)))**(1/2)

    # TODO add print outs for these
    Pt = Pc*(2/(y+1))**(y/(y-1))  # pressure at the throat
    print('Pt: ' + str(Pt))
    Tt = Tc*(Pt/Pc)**((y-1)/y)  # temperature at the throat
    Vt = (R*Tt)/(144*Pt)  # flow specific volume at the throat
    at = np.sqrt(g*y*R*Tt)  # velocity of sound at the throat
    # flow velocity at the throat
    vt = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Pt/Pc)**((y-1)/y)))
    Mt = vt/at  # Mach number at the throat
    print('vt: ' + str(vt))
    print('Mt (this number should be one): ' + str(Mt))

    At2 = (144*mdot*Vt)/vt  # double check throat area with secondary equation
    print('At2: ' + str(At2) + ' ' + AU)

    # Pe1 = Pc*(1-(((y-1)*At**2))/(y+1))**(y/(y-1)) #exit pressure (written equation)
    # Pe2 = (Pc**((y - 1.0)/y)*(-At**2*y + At**2 + y + 1.0)/(y + 1.0))**(y/(y - 1)) #exit pressure (sympy equation)
    # Pe = (Pc*(2**(-1/(y - 1))*At*E*(1/(y + 1))**(-1/(y - 1)))**(-y))
    Pe = float(input('Pe (as close as you can get to outside pressure): '))

    # flow velocity at the nozzle exit
    ve = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Pe/Pc)**((y-1)/y)))
    Te = Tc*((Pe/Pc)**((y-1)/y))
    ae = np.sqrt(g*y*R*Te)
    Me = ve/ae
    print('ve: ' + format(ve.real) + ' ' + VU)
    print('Te: ' + str(Te))
    print('ae: ' + str(ae))
    print('Me: ' + str(Me))

    #E = [(C**(-1/y)*(2*C*R*g - C*R - V**2)/(R*(2*g - 1)))**(y/(y - 1))]

    # weight flow rate TODO add units
    Wdot = At*Pc*np.sqrt((g*y*(2/(y+1))**(y+1)/(y-1))/(R*Tc))
    print('Wdot: ' + str(Wdot))

    MiL = float(input('The lower end of Mi: '))
    MiH = float(input('The higher end of Mi: '))
    TiL = Tc/(1+(0.5*(y-1))*(MiL**2))  # Temperature at nozzle inlet (low)
    TiH = Tc/(1+(0.5*(y-1))*(MiH**2))  # Temperature at nozzle inlet (high)
    aiL = np.sqrt(g*y*R*TiL)  # velocity of sound at the nozzle inlet (low)
    aiH = np.sqrt(g*y*R*TiH)  # velocity of sound at the nozzle inlet (high)
    viL = MiL*aiL  # flow velocity out of the nozzle inlet (low)
    viH = MiH*aiH  # flow velocity out of the nozzle inlet (high)
    PinjL = Pc*((1+(y*(MiL**2)))/((1+((y+1)/2)*(MiL**2))**(y/(y-1))))
    PiL = PinjL/(1+(y*(MiL**2)))
    PinjH = Pc*((1+(y*(MiH**2)))/((1+((y+1)/2)*(MiH**2))**(y/(y-1))))
    PiH = PinjH/(1+(y*(MiH**2)))
    ViL = (R*TiL)/(144*PiL)
    ViH = (R*TiH)/(144*PiH)

    AiL = (144*Wdot*ViL)/viL
    AiH = (144*Wdot*ViH)/viH
    DiL = 2*(np.sqrt(AiL/pi))
    DiH = 2*(np.sqrt(AiH/pi))
    print('AiL: ' + str(AiL))
    print('AiH: ' + str(AiH))
    print('DiL: ' + str(DiL))
    print('DiH: ' + str(DiH))

    Ae = ((2/(y+1))**1/(y-1))*((Pc/Pe)**(1/y))  # Area of nozzle exit
    ε = Ae/At  # Expansion Ratio
    print('Ae: ' + format(Ae.real) + ' ' + AU)
    De = 2*(np.sqrt(Ae/pi))
    print('De: ' + str(De) + ' ' + 'in')
    print('ε: ' + format(ε.real))

    # print('\nNext, Area at any point between the nozzle inlet and nozzle exit') #TODO make a graph or equation in order to easily model
    # Px = None #TODO
    # Tx = Tc*((Px/Pc)**((y-1)/y))
    # Mx = vx/ax #TODO make a vx and ax calculator
    # Ax1 = (At/Mx)*np.sqrt(((1+((y-1)/2)*Mx)/(y+1)/2)**((y+1)/(y-1)))
    # print('Ax1: ' + str(Ax1) + ' ' + AU)

    # # expr = ((((2/(y+1))**(1/(y-1)))*(Pc/Pe)**(1/y))/(sqrt(((y+1)/(y-1))*(1-(Pe/Pc)**((y-1)/y)))))

    # print('\nNext, Area at any point between the nozzle inlet and nozzle throat') #TODO make a graph or equation in order to easily model
    # Px = float(input('Pressure at X (TODO): ')) #Pressure at X TODO find equation
    # Ax2 = At*((((2/(y+1))*(Pc/Px)**((y-1)/y))**((y+1)/(2*(y-1)))))/np.sqrt((2/(y-1))*((Pc/Px)**((y-1)/y)-1))
    # print('Ax2: ' + str(Ax2) + ' ' + AU)

    # print('\nNext, Area at any point between the nozzle throat and nozzle exit') #TODO make a graph or equation in order to easily model
    # Px1 = float(input('Pressure at X (TODO): ')) #Pressure at X TODO find equation
    # Ax3 = At*((((2/(y+1))*(Pc/Px)**(1/y)))/np.sqrt(((y+1)/(y-1))*(1-(Px/Pc)**((y-1)/y))))
    # print('Ax3: ' + str(Ax3) + ' ' + AU)

    # print('\nNext, velocity at any point between nozzle throat and nozzle exit')
    # vx = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Px/Pc)**((y-1)/y))) #Flow velocity at X
    # print('Vx: ' + str(vx) + ' ' + VU)

    variables = [F, Cf, Pc, At, At2, Mo, y, R, Tc, Pt, Tt, Vt, at, vt, Mt, Pe, ve, Te, ae, Me, Wdot, MiL,
                 MiH, TiL, TiH, aiL, aiH, viL, viH, PinjL, PinjH, PiL, PiH, ViL, ViH, AiL, AiH, DiL, DiH, Ae, ε, De]
    names = ['F (Thrust)', 'Cf (Coefficient of Thrust)', 'Pc (Chamber Pressure)', 'At (Throat Area)', 'At2 (Throat Area 2)', 'M (Molecular Weight)', 'y (Specific Heat ratio)', 'R (Gas constant)', 'Tc (Chamber Temperature)', 'Pt (Throat Pressure)', 'Tt (Throat Temperature)', 'Vt (Throat Flow Volume)', 'a (Throat Sound Velocity)', 'vt (Throat Flow Velocity)', 'Mt (Throat Mach Number)',  'Pe (Exit Pressure)', 've (Exit Flow Velocity)', 'Te (Exit Temperature)', 'ae (Exit Sound Velocity)', 'Me (Exit Mach Number)', 'Wdot (Weight Flow Rate)', 'Mi_Lower (Lower Inlet Mach Number)', 'Mi_Higher (Higher Inlet Mach Number)',
             'Ti_Lower (Lower Inlet Temperature)', 'Ti_Higher (Higher Inlet Temperature)', 'ai_Lower (Lower Inlet Sound Velocity)', 'ai_Higher (Higher Inlet Sound Velocity)', 'vi_Lower (Lower Inlet Flow Velocity)', 'vi_Higher (Higher Inlet Flow Velocity)', 'Pinj_Lower (Lower Injector Pressure)', 'Pinj_Higher (Higher Injector Pressure)', 'Pi_Lower (Lower Inlet Pressure)', 'Pi_Higher (Higher Inlet Pressure)', 'Vi_Lower (Lower Inlet Flow Volume)', 'Vi_Higher (Higher Inlet Flow Volume)', 'Ai_Lower (Lower Inlet Area)', 'Ai_Higher (Higher Inlet Area)', 'Di_Lower (Lower Inlet Diameter)', 'Di_Higher (Higher Inlet Diameter)', 'Ae (Exit Area)', 'ε (Expansion Ratio)', 'De (Exit Diameter)']
    equations = e.pretty(['Predetermined', 'Propellant Info', 'Predetermined', 'At = F/(Cf*Pc)', 'At2 = (144*mdot*Vt)/vt', 'Propellant Info', 'Propellant Info', 'R = (1544/M)', 'Temp of Combustion', 'Pt = Pc*(2/(y+1))**(y/(y-1))', 'Tt = Tc*(Pt/Pc)**((y-1)/y)', 'Vt = (R*Tt)/(144*Pt)', 'at = np.sqrt(g*y*R*Tt)', 'vt = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Pt/Pc)**((y-1)/y)))', 'Mt = vt/at', 'Approximate Outside Pressure', 've = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Pe/Pc)**((y-1)/y)))', 'Te = Tc*((Pe/Pc)**((y-1)/y))', 'ae = np.sqrt(g*y*R*Te)', 'Me = ve/ae', 'Wdot = At*Pc*np.sqrt((g*y*(2/(y+1))**(y+1)/(y-1))/(R*Tc))', 'Predetermined Estimate',
                          'Predetermined Estimate', 'TiL = Tc/(1+(0.5*(y-1))*(MiL**2))', 'TiH = Tc/(1+(0.5*(y-1))*(MiH**2))', 'aiL = np.sqrt(g*y*R*TiL)', 'aiH = np.sqrt(g*y*R*TiH)', 'viL = MiL*aiL', 'viH = MiH*aiH', 'PinjL = Pc*((1+(y*(MiL**2)))/((1+((y+1)/2)*(MiL**2))**(y/(y-1))))', 'PiL = PinjL/(1+(y*(MiL**2)))', 'PinjH = Pc*((1+(y*(MiH**2)))/((1+((y+1)/2)*(MiH**2))**(y/(y-1))))', 'PiH = PinjH/(1+(y*(MiH**2)))', 'ViL = (R*TiL)/(144*PiL)', 'ViH = (R*TiH)/(144*PiH)', 'AiL = (144*Wdot*ViL)/viL', 'AiH = (144*Wdot*ViH)/viH', 'DiL = 2*(np.sqrt(AiL/pi))', 'DiH = 2*(np.sqrt(AiH/pi))', 'Ae = ((2/(y+1))**1/(y-1))*((Pc/Pe)**(1/y))', 'ε = Ae/At', 'De = 2*(np.sqrt(Ae/pi))'])

    sheet = input('Would you like a excel spreadsheet? y/n ')
    if sheet == 'y':
        e.sheet(variables, names, equations, 'CC')

    r.restart()
