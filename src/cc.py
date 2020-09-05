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
    Mo = float(input('Molecular weight of combustion products, 23.3M: '))
    y = float(input('Specific heat ratio (Cp/Cv), 1.24: '))
    R = (1544/Mo)  # Gas Constant (ft/deg R)
    Tc = float(input('Temperature of combustion (' + u.TU + '): '))

    # * Throat Params
    Pt = Pc*(2/(y+1))**(y/(y-1))  # pressure at the throat
    print('Pt: ' + str(Pt))
    Tt = Tc*(Pt/Pc)**((y-1)/y)  # temperature at the throat
    Vt = (R*Tt)/(144*Pt)  # flow specific volume at the throat
    at = np.sqrt(y*R*Tt)  # velocity of sound at the throat
    # flow velocity at the throat
    vt = np.sqrt(((2*u.g*y)/(y-1))*R*Tc*(1-(Pt/Pc)**((y-1)/y)))
    Mt = vt/at  # Mach number at the throat
    print('vt: ' + str(vt))
    print('Mt (this number should be one): ' + str(Mt))

    At2 = (144*mdot*Vt)/vt  # double check throat area with secondary equation
    print('At2: ' + str(At2) + ' ' + u.AU)

    # * Nozzle Exit Params
    Pe = float(input('Pe (as close as you can get to outside pressure): '))
    # flow velocity at the nozzle exit

    # TODO add units
    # * Wdot
    Wdot = At*Pc*np.sqrt((u.g*y*(2/(y+1))**(y+1)/(y-1))/(R*Tc))
    print('Wdot: ' + str(Wdot))

    # * Inlet Params
    Mi = float(input('Mi: '))
    Ti = Tc/(1+(0.5*(y-1))*(Mi**2))  # Temperature at nozzle inlet
    ai = np.sqrt(y*R*Ti)  # velocity of sound at the nozzle inlet (low)
    vi = Mi*ai  # flow velocity out of the nozzle inlet (low)
    Pinj = Pc*((1+(y*(Mi**2)))/((1+((y+1)/2)*(Mi**2))**(y/(y-1))))
    Pi = Pinj/(1+(y*(Mi**2)))
    Vi = (R*Ti)/(144*Pi)
    Ai = (144*Wdot*Vi)/vi
    Di = 2*(np.sqrt(ai/pi))
    print('ai: ' + str(ai))
    print('Ai: ' + str(Ai))
    print('Di: ' + str(Di))

    ve = np.sqrt(((2*y)/(y-1))*R*Tc*(1-(Pe/Pc)**((y-1)/y)) + vi**2)
    # F = mdot*v2 + P2Ae; p2 = Pe
    Te = Tc*((Pe/Pc)**((y-1)/y))  # temperature at nozzle exit
    ae = np.sqrt(y*R*Te)  # velocity of sound at nozzle exit
    Me = ve/ae  # Mach Number at nozzle exit
    ε = float(input('ε: '))
    # Ae = ((2/(y+1))**1/(y-1))*((Pc/Pe)**(1/y))  # Area of nozzle exit #! check this
    Ae = ε*At
    print('Ae: ' + format(Ae.real) + ' ' + u.AU)
    De = 2*(np.sqrt(Ae/pi))
    print('De: ' + str(De) + ' ' + 'in')
    print('ε: ' + format(ε.real))
    print('ve: ' + format(ve.real) + ' ' + u.vU)
    print('Te: ' + str(Te))
    print('ae: ' + str(ae))
    print('Me: ' + str(Me))
    Ae2 = (At/Me)*((1+((y-1)/2)*(Me**2))/((y+1)/2))**((y+1)/(2*(y-1)))
    De2 = 2*(np.sqrt(Ae2/pi))
    print('De2: ' + str(De2) + ' ' + 'in')
    ε2 = Ae2/At
    print('Ae2: ' + format(Ae2.real) + ' ' + u.AU)
    print('ε2: ' + str(ε2))

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

    # * Excel Output

    variables = [F, Cf, Pc, At, At2, Mo, y, R, Tc, Pt, Tt, Vt, at, vt, Mt, Pe, ve, Te, ae, Me, Wdot, Mi, MiH, Ti, TiH, ai, aiH, viL, viH, PinjL, PinjH,
                 PiL, PiH, ViL, ViH, ai, AiH, DiL, DiH, Ae, ε, De, Lstar, Vc, ODc, LT, TT, IDc, Lc, Rt, R1, R2, ang, λ, Ln, BLn_8, BLn_75, BLn_7, θn, θe]
    names = ['F (Thrust)', 'Cf (Coefficient of Thrust)', 'Pc (Chamber Pressure)', 'At (Throat Area)', 'At2 (Throat Area 2)', 'M (Molecular Weight)', 'y (Specific Heat ratio)', 'R (Gas constant)', 'Tc (Chamber Temperature)', 'Pt (Throat Pressure)', 'Tt (Throat Temperature)', 'Vt (Throat Flow Volume)', 'a (Throat Sound Velocity)', 'vt (Throat Flow Velocity)', 'Mt (Throat Mach Number)',  'Pe (Exit Pressure)', 've (Exit Flow Velocity)', 'Te (Exit Temperature)', 'ae (Exit Sound Velocity)', 'Me (Exit Mach Number)', 'Wdot (Weight Flow Rate)', 'Mi_Lower (Lower Inlet Mach Number)', 'Mi_Higher (Higher Inlet Mach Number)',
             'Ti_Lower (Lower Inlet Temperature)', 'Ti_Higher (Higher Inlet Temperature)', 'ai_Lower (Lower Inlet Sound Velocity)', 'ai_Higher (Higher Inlet Sound Velocity)', 'vi_Lower (Lower Inlet Flow Velocity)', 'vi_Higher (Higher Inlet Flow Velocity)', 'Pinj_Lower (Lower Injector Pressure)', 'Pinj_Higher (Higher Injector Pressure)', 'Pi_Lower (Lower Inlet Pressure)', 'Pi_Higher (Higher Inlet Pressure)', 'Vi_Lower (Lower Inlet Flow Volume)', 'Vi_Higher (Higher Inlet Flow Volume)', 'Ai_Lower (Lower Inlet Area)', 'Ai_Higher (Higher Inlet Area)', 'Di_Lower (Lower Inlet Diameter)', 'Di_Higher (Higher Inlet Diameter)', 'Ae (Exit Area)', 'ε (Expansion Ratio)', 'De (Exit Diameter)', 'Characteristic Length (L*)', 'Chamber Volume (Vc)', 'Chamber Outer Diameter (ODc)', 'Ablative Liner Thickness (LT)', 'Chamber Tube Thickness (TT)', 'Chamber Inner Diameter (IDc)', 'Chamber Length (Lc)', 'Throat Radius (Rt)', 'Radius Before Throat (R1)', 'Radius After Throat (R2)', 'Connical Half Angle', 'Lambda (λ)', 'Connical Nozzle Length (Ln)', '80% Bell Nozzle Length (BLn_8)', '75* Bell Nozzle Length (BLn_75)', '70% Bell Nozzle Length (BLn_7)', 'Parabola Entry Angle (θn)', 'Parabola Exit Angle (θe)']
    equations = e.pretty([e.P, e.PI, e.P, 'At = F/(Cf*Pc)', 'At2 = (144*mdot*Vt)/vt', e.PI, e.PI, 'R = (1544/M)', 'Temp of Combustion', 'Pt = Pc*(2/(y+1))**(y/(y-1))', 'Tt = Tc*(Pt/Pc)**((y-1)/y)', 'Vt = (R*Tt)/(144*Pt)', 'at = np.sqrt(g*y*R*Tt)', 'vt = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Pt/Pc)**((y-1)/y)))', 'Mt = vt/at', 'Approximate Outside Pressure', 've = np.sqrt(((2*g*y)/(y-1))*R*Tc*(1-(Pe/Pc)**((y-1)/y)))', 'Te = Tc*((Pe/Pc)**((y-1)/y))', 'ae = np.sqrt(g*y*R*Te)', 'Me = ve/ae', 'Wdot = At*Pc*np.sqrt((g*y*(2/(y+1))**(y+1)/(y-1))/(R*Tc))', e.PE, e.PE, 'Ti = Tc/(1+(0.5*(y-1))*(Mi**2))', 'TiH = Tc/(1+(0.5*(y-1))*(MiH**2))', 'ai = np.sqrt(g*y*R*Ti)', 'aiH = np.sqrt(g*y*R*TiH)', 'viL = Mi*ai', 'viH = MiH*aiH', 'PinjL = Pc*((1+(y*(Mi**2)))/((1+((y+1)/2)*(Mi**2))**(y/(y-1))))',
                          'PiL = PinjL/(1+(y*(Mi**2)))', 'PinjH = Pc*((1+(y*(MiH**2)))/((1+((y+1)/2)*(MiH**2))**(y/(y-1))))', 'PiH = PinjH/(1+(y*(MiH**2)))', 'ViL = (R*Ti)/(144*PiL)', 'ViH = (R*TiH)/(144*PiH)', 'ai = (144*Wdot*ViL)/viL', 'AiH = (144*Wdot*ViH)/viH', 'DiL = 2*(np.sqrt(ai/pi))', 'DiH = 2*(np.sqrt(AiH/pi))', 'Ae = ((2/(y+1))**1/(y-1))*((Pc/Pe)**(1/y))', 'ε = Ae/At', 'De = 2*(np.sqrt(Ae/pi))', e.PE, 'Vc = At*Lstar', e.P, e.P, e.P, 'IDc = ODc - (2*LT) - (2*TT)', 'Lc = Vc/(pi*(IDc**2))', 'Rt = np.sqrt(At/pi)', 'R1 = Rt', 'R2 = 0.382 * Rt ', e.PE, 'λ=0.5*(1+cos(ang))', 'Ln = (Rt*((np.sqrt(ε)-1))+(R1*cos(ang-1))**-1)) / np.tan(np.(ang))', '0.8 * Ln', '0.75 * Ln', '0.7 * Ln', (e.PE + 'based off ε and Bell Percentage'), (e.PE + 'based off ε and Bell Percentage')])
    units = [u.FU, e.NU, u.PU, u.AU, u.AU, u.Mo, e.NU, 'ft/R°', u.TU, u.PU, u.TU, u.VU, u.aU, u.vU, e.NU, u.PU, u.vU, u.TU, u.aU, e.NU, 'lb/sec', e.NU, e.NU, u.TU, u.TU, u.aU, u.aU, u.vU, u.vU,
             u.PU, u.PU, u.PU, u.PU, u.VU, u.VU, u.AU, u.AU, u.DU, u.DU, u.AU, e.NU, u.DU, u.DU, u.VoU, u.DU, u.DU, u.DU, u.DU, u.DU, u.DU, u.DU, u.DU, u.ang, e.NU, u.DU, u.DU, u.DU, u.DU, u.ang, u.ang]

    sheet = input('Would you like a excel spreadsheet? y/n ')
    if sheet == 'y':
        e.sheet(variables, names, units, equations, 'CC')

    r.restart()
