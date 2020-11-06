# Calculatre injector parameters based upon what is found in the nasa document
import numpy as np
import restart as r
import excel as e
import units as u
pi = np.pi


def run():
    print("\nWelcome to the Injector Calculator!")
    print("Here you can find mass flow, the size of the injector outlets, accurate Chamber pressure (P1/Pc), the ratio between oxygen and fuel velocities, and the ratio between oxygen and fuel pressures\n")

    print('Recommendations/Equation Requirements: \nImpingement angle of 60 degrees\n0.79 ratio between ID/OD of outlets (uneven triplets)')

    print('\nFor this, first we will determine total mass flow (mdot)')
    F = float(input('F (Thrust): '))
    Is = float(input('Isp (specific impulse): '))
    if(u.system == '1'):
        mdot = F/(go*Is)
    if(u.system == '2'):
        mdot = F/Is
    print('\nmdot = ' + str(mdot) + ' ' + u.MdU)

    oxHoles = float(input('Oxidizer Holes: '))
    fuelHoles = float(input('Fuel Holes: '))

    print('\nNext, we will determine the area and therefore diameter of the injector outlets, starting with the oxidizer')
    Cd = float(input('Cd (density coefficient, recommended 0.6): '))
    oxidizerP = float(input('p of the oxidizer: '))
    deltap = float(input('delta-p across injector (recommended 70 psi): '))
    fuelP = float(input('p of the fuel: '))
    mixRatio = float(input('Mixture Ratio: '))
    oxMdot = (mixRatio*mdot)/(mixRatio + 1)
    fuelMdot = mdot/(mixRatio + 1)
    print('Oxygen Mass Flow Rate: ' + str(oxMdot))
    print('Fuel Mass Flow Rate: ' + str(fuelMdot))
    print(oxMdot/fuelMdot)

    oxidizerArea = oxMdot/(Cd*np.sqrt(2*u.g*oxidizerP*deltap))
    fuelArea = fuelMdot/(Cd*np.sqrt(2*u.g*fuelP*deltap))
    print('\nTotal Oxidizer Hole Area: ' + str(oxidizerArea))
    individualOxArea = oxidizerArea / oxHoles
    print('Individual Oxygen Hole Area: ' + str(individualOxArea))
    print('Total Fuel Hole Area: ' + str(fuelArea))
    individualFuelArea = fuelArea / fuelHoles
    print('Individual Fuel Hole Area: ' + str(individualFuelArea))

    oxDiameter = 2*np.sqrt(individualOxArea/pi)
    fuelDiameter = 2*np.sqrt(individualFuelArea/pi)
    print('\nThe diameter of each oxidizer hole is ' + str(oxDiameter) +
          ' in\nand the diameter of each fuel hole is ' + str(fuelDiameter) + ' in')

    variables = [F, Is, mdot, oxHoles, fuelHoles, Cd, oxidizerP, deltap,
                 fuelP, mixRatio, fuelArea, individualOxArea, individualFuelArea, oxDiameter, fuelDiameter]
    names = ['F (thrust)', 'Is (Specific Impulse', 'mdot (Mass Flow Rate)', 'Element Count', 'Injector Type', 'Oxidizer Holes', 'Fuel Holes', 'Cd (Density Coefficient)', 'p_o (Oxidizer Density)', 'delatp (Pressure Change over Injecor)', 'TOA (Total Oxidizer Hole Area)', 'IOA (Individual Oxidizer Hole Area)', 'p_f (Fuel Density)', 'TFA (Total Fuel Hole Area)',
             'IFA (Individual Fuel Hole Area)', 'Do (Individual Oxidizer Hole Diameter', 'Df (Individual Fuel Hole Diameter', 'Mixture Ratio (fuel: oxidizer)', 'TROA (Total Ratioed Oxidizer Area)', 'fuelArea (Total Ratioed Fuel Area)', 'individualOxArea (Individual Ratioed Oxidizer Area)', 'individualFuelArea (Individual Ratioed Fuel Area)', 'oxDiameter (Ratioed Oxidizer Hole Diameter)', 'fuelDiameter (Ratioed Fuel Hole Diameter']
    equations = e.pretty([e.P, e.PI, 'mdot = F/Is', e.PE, e.P, e.PE, e.PE, e.PE, e.PI, e.PE, 'TOA = mdot/(Cd*np.sqrt(2*go*oxidizerP*deltap))', 'IOA = TOA / o-hole-count',
                          e.PI, 'TFA = mdot/(Cd*np.sqrt(2*go*fuelP*deltap))', 'IFA = TFA / f-hole-count', 'Do = 2*np.sqrt(IOA/pi)', 'Df = 2*np.sqrt(IFA/pi)', e.PI, 'TROA = oxMdot/(Cd*np.sqrt(2*go*oxidizerP*deltap))', 'fuelArea = fuelMdot/(Cd*np.sqrt(2*go*oxidizerP*deltap))', 'individualOxArea = TROA / o-hole-count', 'individualFuelArea = fuelArea / o-hole-count', 'oxDiameter = 2*np.sqrt(individualOxArea/pi)', 'fuelDiameter = 2*np.sqrt(individualFuelArea/pi)'])
    units = [u.FU, e.NU, u.MdU, e.NU, e.NU, e.NU, e.NU, e.NU, u.pgU, u.PU, u.AU,
             u.AU, u.pgU, u.AU, u.AU, u.DU, u.DU, e.NU, u.AU, u.AU, u.AU, u.AU, u.DU, u.DU]

    sheet = input('Would you like a excel spreadsheet? y/n ')
    if sheet == 'y':
        e.sheet(variables, names, units, equations, 'Injector')

    r.restart()
