import restart as r
import numpy as np
import sympy as sym
import excel as e
import units as u

# TODO add print outs for everything


def run():
    print("\nWelcome to the Combustion Chamber Calculator! \n")
    print("Here you can find thrust (F), coefficient of thrust (Cf), Chamber Pressure (Pc) or Throat Area (At) when you know at least three of these values.\n")

    pi = np.pi

    # * Throat Area
    F = float(input("F (" + u.FU + "): "))
    Cf = float(input("Cf: "))
    Pc = float(input("Pc estimate (" + u.PU + "): "))
    At = F/(Cf*Pc)
    print("At: " + str(At) + ' ' + u.AU)

    # * Mdot
    Is = float(input('Isp (specific impulse): '))
    if(u.system == '1'):
        mdot = F/(u.g*Is)
    else:
        mdot = F/Is
    print('\nmdot = ' + str(mdot) + ' ' + u.MdU)

    # * Various Variables
    Mo = float(input('Molecular weight of combustion products, 23.3M: '))  # ! Fix
    y = float(input('Specific heat ratio (Cp/Cv), 1.24: '))  # ! Fix
    R = (1544/Mo)  # Gas Constant (ft/deg R)
    RInch = 12*(1544/Mo)
    Tc = float(input('Temperature of combustion (' + u.TU + '): '))

    # * Nozzle Exit Params
    Pe = float(input('Pe (as close as you can get to outside pressure): '))
    # flow velocity at the nozzle exit

    # TODO add units
    # * Wdot
    Wdot = At*Pc*np.sqrt((u.g*y*(2/(y+1))**(y+1)/(y-1)) /
                         (R*Tc))  # ! Not in Sutton
    print('Wdot: ' + str(Wdot))

    # * Inlet Params
    Mi = float(input('Mi: '))  # !

    # Ti = Tc/(1+(0.5*(y-1))*(Mi**2))  # ! NON SUTTON Temperature at nozzle inlet
    Ti = Tc  # Sutton book

    # ai = np.sqrt(y*R*Ti)  # velocity of sound at the nozzle inlet (low) # ! NON SUTTON
    # vi = Mi*ai  # flow velocity out of the nozzle inlet (low) # ! NON SUTTON

    ai = np.sqrt(y*R*Ti)
    vi = Mi*ai

    Pinj = Pc*((1+(y*(Mi**2)))/((1+((y+1)/2)*(Mi**2))**(y/(y-1))))  # !
    Pi = Pinj/(1+(y*(Mi**2)))  # !
    Vi = (R*Ti)/(144*Pi)  # !
    Ai = (144*Wdot*Vi)/vi  # !
    Di = 2*(np.sqrt(ai/pi))
    print('ai: ' + str(ai))
    print('Ai: ' + str(Ai))
    print('Di: ' + str(Di))

    ve = np.sqrt(((2*y)/(y-1))*R*Tc*(1-(Pe/Pc)**((y-1)/y)) + vi**2)
    # F = mdot*v2 + P2Ae; p2 = Pe
    Te = Tc*((Pe/Pc)**((y-1)/y))  # ! temperature at nozzle exit
    ae = np.sqrt(y*R*Te)  # velocity of sound at nozzle exit
    Me = ve/ae  # Mach Number at nozzle exit
    # Area of nozzle exit #! check this
    # Ae = ((2/(y+1))**1/(y-1))*((Pc/Pe)**(1/y))  # !broken
    # print('Ae: ' + format(Ae.real) + ' ' + u.AU)
    # De = 2*(np.sqrt(Ae/pi))
    # print('De: ' + str(De) + ' ' + 'in')
    # ε = Ae/At
    # print('ε: ' + format(ε.real))

    print('ve: ' + format(ve.real) + ' ' + u.vU)
    print('Te: ' + str(Te))
    print('ae: ' + str(ae))
    print('Me: ' + str(Me))
    Ae = (At/Me)*((1+((y-1)/2)*(Me**2))/((y+1)/2))**((y+1)/(2*(y-1)))
    De = 2*(np.sqrt(Ae/pi))
    print('De: ' + str(De) + ' ' + 'in')
    ε = Ae/At
    print('Ae: ' + format(Ae.real) + ' ' + u.AU)
    print('ε: ' + str(ε))

    # Ae3 = At/((((y+1)/2)**(1/(y-1)))*((Pe/Pc)**(1/y)) *
    #           np.sqrt(((y+1)/(y-1))*((1-(Pe/Pc))**((y-1)/y))))
    # De3 = 2*(np.sqrt(Ae3/pi))
    # print('De3: ' + str(De3) + ' ' + 'in')
    # ε3 = Ae3/At
    # print('Ae3: ' + format(Ae3.real) + ' ' + u.AU)
    # print('ε3: ' + str(ε3))

    # * Nozzle/Chamber Geom Params
    Lstar = float(input('Characteristic Length (L*): '))
    Vc = At*Lstar
    print('Vc: ' + str(Vc))
    # Lstar = Mdot*V*ts/At
    # Lstar between 40-50in
    # 23k y1
    ODc = float(input('Outer Diameter of the combustion chamber: '))
    LT = float(input('Ablative Liner Thickness: '))
    TT = float(input('Tube Thickness: '))
    IDc = ODc - (2*LT) - (2*TT)
    Lc = Vc/(pi*((IDc/2)**2))
    Ac = pi*(IDc/2)**2
    ContractionRatio = (Ac/At)
    print('Chamber Inner Diameter: ' + str(IDc))
    print('Chamber Length: ' + str(Lc))

    # ? surface area of the nozzle pdf page 101

    Rt = np.sqrt(At/pi)
    print('Rt: ' + str(Rt))
    R1 = Rt  # range from 0.5 to 1.5 of Rt (before Throat)
    R2 = 0.382 * Rt  # After throat
    print('R1 (before throat): ' + str(R1))
    print('R2 (after throat): ' + str(R2))

    # ? half angle between 20-45

    ang = float(input(
        'Half angle of the Conical Nozzle (usually 15): '))
    λ = 0.5*(1+np.cos(np.radians(ang)))
    print('λ: ' + str(λ))
    sec = (np.cos(np.radians(ang-1)))**-1
    tan = np.tan(np.radians(ang))
    Ln = (Rt*((np.sqrt(ε)-1))+(R1*sec)) / tan
    print('Optimum Conical Nozzle length (Ln): ' + str(Ln))
    BLn_8 = Ln * 0.8
    BLn_75 = Ln * 0.752
    BLn_7 = Ln * 0.7
    print('80% Bell Nozzle Length (Ln): ' + str(BLn_8))
    print('75% Bell Nozzle Length (Ln): ' + str(BLn_75))
    print('70% Bell Nozzle Length (Ln): ' + str(BLn_7))
    θn = float(input('θn (~27): '))
    θe = float(input('θe (~13): '))

    # * Throat Params
    Pt = Pc*(2/(y+1))**(y/(y-1))  # ^ pressure at the throat
    print('Pt: ' + str(Pt))

    # Tt = Tc*(Pt/Pc)**((y-1)/y)  # !temperature at the throat NON SUTTON
    Tt = (2*Tc)/(y+1)  # Sutton version
    # Vt = (R*Tt)/(144*Pt)  # !flow specific volume at the throat NON SUTTON

    V1 = (R*Tc)/(144*Pc)  # Specific Volume
    Vt = V1*((y+1)/2)**(1/(y-1))  # Sutton Version

    at = np.sqrt(y*R*Tt)  # velocity of sound at the throat

    # ! flow velocity at the throat
    # ! why broken now?
    # vt = np.sqrt(((2*u.g*y)/(y-1))*R*Tc*(1-(Pt/Pc)**((y-1)/y))) #!NON SUTTON
    vt = np.sqrt(((2*y)/(y+1))*R*Tc)  # Sutton Version

    Mt = vt/at  # Mach number at the throat #! why broken now?
    print('vt: ' + str(vt))
    print('Mt (this number should be one): ' + str(Mt))

    At2 = (144*mdot*Vt)/vt  # double check throat area with secondary equation
    print('At2: ' + str(At2) + ' ' + u.AU)

    # double check throat area with secondary equation
    # At3 = ft^2, mdot = Lbm/sec, Vt2 = ft^3/lbm, vt2 = ft/sec
    At3 = np.sqrt((144*mdot*Vt)/vt)  # ! understand square root
    print('At3: ' + str(At3) + ' ' + u.AU)

    # * Excel Output

    variables = [F, Cf, Pc, At, At2, Is, mdot, Wdot, Mo, y, R, Tc, Pt, Tt, V1, Vt, at, vt, Mt, Pe, ve, Te, ae, Me, Mi, Ti, ai, vi, Pinj,
                 Pi, Vi, Ai, Di, Ae, ε, De, Lstar, Vc, ODc, LT, TT, IDc, Lc, Rt, ang, λ, Ln, BLn_8, BLn_75, BLn_7, θn, θe]
    names = ['F (Thrust)', 'Cf (Coefficient of Thrust)', 'Pc (Chamber Pressure)', 'At (Throat Area)', 'At2 (Throat Area 2)', 'Is (Specific Impulse)', 'mdot (Mass Flow Rate)', 'Wdot (Weight Flow Rate)', 'M (Molecular Weight)', 'y (Specific Heat ratio)', 'R (Gas constant)', 'Tc (Chamber Temperature)', 'Pt (Throat Pressure)', 'Tt (Throat Temperature)', 'V1 (Specific Volume)', 'Vt (Throat Flow Volume)', 'at (Throat Sound Velocity)', 'vt (Throat Flow Velocity)', 'Mt (Throat Mach Number)',  'Pe (Exit Pressure)', 've (Exit Flow Velocity)', 'Te (Exit Temperature)', 'ae (Exit Sound Velocity)', 'Me (Exit Mach Number)', 'Wdot (Weight Flow Rate)', 'Mi (Inlet Mach Number)',
             'Ti (Inlet Temperature)', 'ai (Inlet Sound Velocity)', 'vi (Inlet Flow Velocity)', 'Pinj (Injector Pressure)', 'Pi (Inlet Pressure)', 'Vi (Inlet Flow Volume)', 'Ai (Inlet Area)', 'Di (Inlet Diameter)', 'Ae (Exit Area)', 'ε (Expansion Ratio)', 'De (Exit Diameter)', 'L* (Characteristic Length)', 'Vc (Chamber Volume)', 'ODc (Chamber Outer Diameter)', 'LT (Ablative Liner Thickness)', 'TT (Chamber Tube Thickness)', 'IDc (Chamber Inner Diameter)', 'Lc (Chamber Length)', 'Rt (Throat Radius)', 'Connical Half Angle', 'Lambda (λ)', 'Ln (Connical Nozzle Lengthz)', '80% Bell Nozzle Length', '75% Bell Nozzle Length', '70% Bell Nozzle Length', 'θn (Parabola Entry Angle)', 'θe (Parabola Exit Angle)']
    equations = e.pretty([e.P, e.PI, e.P, 'At = F/(Cf*Pc)', 'At2 = (144*mdot*Vt)/vt', e.PI, 'mdot = F/Is', 'Wdot = At*Pc*np.sqrt((u.g*y*(2/(y+1))**(y+1)/(y-1))/(R*Tc))', e.PI, e.PI, 'R = (1544/M)', 'Temperature of Combustion', 'Pt = Pc*(2/(y+1))**(y/(y-1))', 'Tt = (2*Tc)/(y+1)', 'V1 = (R*Tc)/(144*Pc)', 'Vt = V1*((y+1)/2)**(1/(y-1))', 'at = np.sqrt(y*R*Tt)', 'vt = np.sqrt(((2*y)/(y+1))*R*Tc)', 'Mt = vt/at', 'Approximate Outside Pressure', 've = np.sqrt(((2*y)/(y-1))*R*Tc*(1-(Pe/Pc)**((y-1)/y)) + vi**2)', 'Te = Tc*((Pe/Pc)**((y-1)/y))', 'ae = np.sqrt(y*R*Te)', 'Me = ve/ae', e.PE, 'Ti = Tc', 'ai = np.sqrt(g*y*R*Ti)', 'vi = Mi*ai', 'Pinj = Pc*((1+(y*(Mi**2)))/((1+((y+1)/2)*(Mi**2))**(y/(y-1))))',
                          'Pi = Pinj/(1+(y*(Mi**2)))', 'Vi = (R*Ti)/(144*Pi)', 'Ai = (144*Wdot*Vi)/vi', 'Di = 2*(np.sqrt(ai/pi))', 'Ae = (At/Me)*((1+((y-1)/2)*(Me**2))/((y+1)/2))**((y+1)/(2*(y-1)))', 'ε = Ae/At', 'De = 2*(np.sqrt(Ae/pi))', e.PE, 'Vc = At*Lstar', e.P, e.P, e.P, 'IDc = ODc - (2*LT) - (2*TT)', 'Lc = Vc/(pi*(IDc**2))', 'Rt = np.sqrt(At/pi)', e.PE, 'λ=0.5*(1+cos(ang))', 'Ln = (Rt*((np.sqrt(ε)-1))+(R1*cos(ang-1))**-1)) / np.tan(np.(ang))', '0.8 * Ln', '0.75 * Ln', '0.7 * Ln', (e.PE + 'based off ε and Bell Percentage'), (e.PE + 'based off ε and Bell Percentage')])
    units = [u.FU, e.NU, u.PU, u.AU, u.AU, u.TimeU, u.MdU, u.WU, u.Mo, e.NU, 'ft/R°', u.TU, u.PU, u.TU, u.VU, u.VU, u.aU, u.vU, e.NU, u.PU, u.vU, u.TU, u.aU, e.NU, e.NU, u.TU, u.aU, u.vU,
             u.PU, u.PU, u.VU, u.AU, u.DU, u.AU, e.NU, u.DU, u.DU, u.VoU, u.DU, u.DU, u.DU, u.DU, u.DU, u.DU, u.ang, e.NU, u.DU, u.DU, u.DU, u.DU, u.ang, u.ang]

    sheet = input('Would you like a excel spreadsheet? y/n ')
    if sheet == 'y':
        e.sheet(variables, names, units, equations, 'CC')

    r.restart()
