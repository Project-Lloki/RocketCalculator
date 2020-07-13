#Calculate apogee from mass, thrust and other fun things
import math

def run():
    print("\nWelcome to the Apogee Calculator! \n")
    print("Here you can find the apogee given dry mass, propellant/oxidizer combined mass and thrust, the optimal dry mass for a given apogee, or the optimal thrust numbers for a mass and burn time \n")
    print("\nChoose the value you wish to calculate for:")
    print("\n 1: Apogee from thrust, burn time, mass, estimated frontal area \n 2:Radius from Height and weight\n")
    solve = input("What are you solving for?\n")

    def apogee():
        dryMass = float(input("Dry mass in lbs : "))
        propellantMass = float(input("propelland + oxidizer mass in lbs : "))
        burnTime = float(input("Burn time in seconds : "))
        thrust = float(input("Thrust in lbf "))
        frontalArea = float(input("Frontal area of rocket : "))
        dragCoeff = float(input("Drag Coefficient (if you don't know, 0.5 is a good estimate)"))


    def radius():
        h = float(input("height-inches:")) / 12
        weight = float(input("weight in pounds:"))
        loxOrKero = input(" LOX or Kerosene \n 1: LOX, 2: Kerosene: \n")
        if loxOrKero == '1':
            volume = 1.5 * (weight / loxWeightPerCubedFoot)
            return format(math.sqrt((volume/(math.pi*h))), '0.3f') + " feet or " + format(math.sqrt((volume/(math.pi*h))) * 12, '0.3f') + " inches"
        elif loxOrKero == '2':
            volume = 1.5 * (weight / keroseneWeightPerCubedFoot)
            return format(math.sqrt((volume/(math.pi*h))), '0.3f') + " feet or " + format(math.sqrt((volume/(math.pi*h))) * 12, '0.3f') + " inches"

    if(solve == '1'):
        print(apogee())
    elif(solve == '2'):
        print(radius())
    else :
        print("Invalid input, use 1 or 2 + ENTER")

