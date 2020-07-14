# tank height and radius calculator from weight requirements for lox and kerosene.
import math

def run():
    print("\nWelcome to the Tank Calculator! \n")
    print("Here you can find the volume of each tank including 1/3 ullage in liquid tanks (Vf), volume of each tank excluding 1/3 ullage (Vi), the inner radius of the tank(r), or the height of the tank (h) when you know at least three of these values.\n")
    print("\nChoose the value you wish to calculate for:")
    print("\n 1: Height from weight and radius. \n 2:Radius from Height and weight\n")
    solve = input("What are you solving for?\n")


    loxWeightPerCubedFoot = 71.23
    keroseneWeightPerCubedFoot = 49.90

    def height():
        r = float(input("radius-inches:"))/12
        weight = float(input("weight in pounds:"))
        loxOrKero = input(" LOX or Kerosene \n 1: LOX, 2: Kerosene: \n")
        if loxOrKero == '1' :
            volume = 1.5 * (weight / loxWeightPerCubedFoot)
            return format(volume / ((r ** 2) * math.pi), '0.3f') + " feet or "  + format((volume / ((r ** 2) * math.pi))*12, '0.3f') + " inches"
        elif loxOrKero == '2' :
            volume = 1.5 * (weight / keroseneWeightPerCubedFoot)
            return format(volume / ((r ** 2) * math.pi), '0.3f') + " feet or "  + format((volume / ((r ** 2) * math.pi))*12, '0.3f') + " inches"

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
        print(height())
    elif(solve == '2'):
        print(radius())
    else :
        print("Invalid input, use 1 or 2 + ENTER")

