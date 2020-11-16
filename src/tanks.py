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

    print("\nChoose the value you wish to calculate for:")
    print("\n 1: Height from weights. \n 2: Height from mdot/burntime/ratio .")
    solve = input("What are you solving for?\n")

    loxWeightPerCubedFoot = 71.23
    keroseneWeightPerCubedFoot = 50.566665
    def volume():
        loxMass = float(input("Lbs of lox: "))
        fuelMass = float(input("Lbs of fuel: "))
        r = float(input("radius-inches: ")) / 12
        ullageF = float(input("% of FUEL tankage you want to be ullage: "))
        ullageO = float(input("% of OXIDIZER tankage you want to be ullage: "))
        loxVolume = (loxMass / loxWeightPerCubedFoot)/(1 - ullageO)
        fuelVolume = (fuelMass / keroseneWeightPerCubedFoot)/(1 - ullageF)
        loxHeightFeet = (loxVolume/(math.pi*r**2)) - (4/3*r)
        loxHeightInches = loxHeightFeet * 12
        fuelHeightFeet =(fuelVolume/(math.pi*r**2)) - (4/3*r)
        fuelHeightInches = fuelHeightFeet * 12
        print(format(loxHeightFeet, '0.3f') + " feet or " + format(loxHeightInches, '0.3f') + " inches")
        print(format(fuelHeightFeet, '0.3f') + " feet or " + format(fuelHeightInches, '0.3f') + " inches")

    def height():
        mdot = float(input("your mdot (mass flow) in lb/s: "))
        ratio = float(input("Mixture (O/F) ratio: "))
        ullageF = float(input("% of FUEL tankage you want to be ullage: "))
        ullageO = float(input("% of OXIDIZER tankage you want to be ullage: "))
        burnTime = float(input("burntime: "))
        fuelMass = (mdot * burnTime)/(ratio + 1)
        loxMass = fuelMass * ratio
        print(format(loxMass, '0.3f') + "lbs LOX and " + format(fuelMass, '0.3f') + "lbs fuel.")
        r = float(input("radius-inches: "))/12
        loxVolume =  (loxMass / loxWeightPerCubedFoot)/(1 - ullageO)
        loxHeightFeet = (loxVolume/(math.pi*r**2)) - (4/3*r)
        loxHeightInches = loxHeightFeet*12
        print(format(loxHeightFeet, '0.3f') + " feet or " + format(loxHeightInches, '0.3f') + " inches")
        fuelVolume =(fuelMass / keroseneWeightPerCubedFoot)/(1-ullageF)
        fuelHeightFeet = (fuelVolume/(math.pi*r**2)) - (4/3*r)
        fuelHeightInches = fuelHeightFeet*12
        print(format(fuelHeightFeet, '0.3f') + " feet or " + format(fuelHeightInches, '0.3f') + " inches")

    if solve == '1':
        volume()
    elif solve == '2':
        height()
    else:
        print('choose a proper calculator')

    re.restart()
