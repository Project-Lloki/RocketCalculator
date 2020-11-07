# tank height and radius calculator from weight requirements for lox and kerosene.
import excel as e
import restart as re
import units as u
import math

variables = []
names = []
equations = []
units = []


def run():
    global variables, names, equations, units
    print("\nWelcome to the Tank Calculator! \n")
    print("Here you can find the volume of each tank including 1/3 ullage in liquid tanks (Vf), volume of each tank excluding 1/3 ullage (Vi), the inner radius of the tank(r), or the height of the tank (h) when you know at least three of these values.\n")

    # print("\nChoose the value you wish to calculate for:")
    # print("\n 1: Height from weight and radius. \n 2:Radius from Height and weight.\n 3: Mass needed for LOX/Kerosene given burn time and mdot.\n ¡")
    # solve = input("What are you solving for?\n")

    loxWeightPerCubedFoot = 71.23
    keroseneWeightPerCubedFoot = 49.90

    mdot = float(input("your mdot (mass flow) in lb/s: "))
    ratio = float(input("Mixture (O/F) ratio: "))
    ullageF = float(input("% of FUEL tankage you want to be ullage: "))
    ullageO = float(input("% of OXIDIZER tankage you want to be ullage: "))
    burnTime = float(input("burntime: "))
    fuelMass = (mdot * burnTime)/(ratio + 1)
    loxMass = fuelMass * ratio
    print(format(loxMass, '0.3f') + "lbs LOX and " +
          format(fuelMass, '0.3f') + "lbs fuel.")

    r = float(input("radius-inches: "))/12
    loxVolume =  (loxMass / loxWeightPerCubedFoot)/(1 - ullageO)

    loxHeightFeet = (loxVolume - (4/3*math.pi*r**2))/(math.pi*r)
    loxHeightInches = loxHeightFeet*12
    print(format(loxHeightFeet, '0.3f') + " feet or " +
          format(loxHeightInches, '0.3f') + " inches")

    fuelVolume =(fuelMass / keroseneWeightPerCubedFoot)/(1-ullageF)
    fuelHeightFeet = fuelVolume / ((r ** 2) * math.pi)
    fuelHeightInches = (fuelVolume / ((r ** 2) * math.pi))*12
    print(format(fuelHeightFeet, '0.3f') + " feet or " + format(fuelHeightInches, '0.3f') + " inches")


    variables = [mdot, burnTime, fuelMass, loxMass, r,
                 loxVolume, loxHeightInches, fuelVolume, fuelHeightInches]
    names = ['Mass Flow Rate (mdot)', 'Burntime', 'Kerosene Mass', 'LOX Mass', 'Tank Radius', 'LOX Tank Volume',
             'LOX Tank Height', 'Kerosene Tank Volume', 'Kerosene Tank Height']
    equations = [e.P, e.P, 'fuelMass = (mdot * burnTime)/3.56', 'loxMass = fuelMass * 2.56', e.P, 'lox Volume = 1.5 * (weight / PropellantDensity)',
                 'lox Height = (volume / ((r ** 2) * math.pi))*12', 'kerosene Volume = 1.5 * (weight / PropellantDensity)', 'kerosene Height = (volume / ((r ** 2) * math.pi))*12']
    units = [u.MdU, u.TimeU, u.WU, u.WU, u.DU, u.VoU, u.DU, u.VoU, u.DU]

    # def radius():
    #     global variables, names, equations, units
    #     h = float(input("height-inches:")) / 12
    #     weight = float(input("weight in pounds:"))
    #     loxOrKero = input(" LOX or Kerosene \n 1: LOX, 2: Kerosene: \n")
    #     if loxOrKero == '1':
    #         volume = 1.5 * (weight / loxWeightPerCubedFoot)
    #         return format(math.sqrt((volume/(math.pi*h))), '0.3f') + " feet or " + format(math.sqrt((volume/(math.pi*h))) * 12, '0.3f') + " inches"
    #     elif loxOrKero == '2':
    #         volume = 1.5 * (weight / keroseneWeightPerCubedFoot)
    #         return format(math.sqrt((volume/(math.pi*h))), '0.3f') + " feet or " + format(math.sqrt((volume/(math.pi*h))) * 12, '0.3f') + " inches"

    # if(solve == '1'):
    #     print(height())
    # elif(solve == '2'):
    #     print(radius())
    # elif(solve == '3'):
    #     print(fuelNeeded())
    # else:
    #     print("Invalid input, use 1 or 2 + ENTER")

    sheet = input('Would you like a excel spreadsheet? y/n ')
    if sheet == 'y':
        e.sheet(variables, names, units, equations, 'Tanks')

    re.restart()
