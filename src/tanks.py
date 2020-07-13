# coding=utf-8
import numpy as np
import math

def run():
    print("\nWelcome to the Tank Calculator! \n")
    print("Here you can find the volume of each tank including 1/3 ullage in liquid tanks (Vf), volume of each tank excluding 1/3 ullage (Vi), the inner radius of the tank(r), or the height of the tank (h) when you know at least three of these values.\n")
    FU = 'N'
    PU = ''
    AU = ''
    print("\nChoose the value you wish to calculate for:")
    print("\n 1: Tank dimensions from weight and radius. \n 2:  XXXX NOT DONE Cf (Coefficient of thrust) \n 3: Pc(Chamber Pressure) \n 4: At (Throat area)\n")
    solve = input("What are you solving for?")


    loxWeightPerCubedFoot = 71.23
    keroseneWeightPerCubedFoot = 49.9

    def heightFromWeightandRadius():
        r = float(input("radius-inches:"))
        weight = float(input("weight in pounds:"))
        loxOrKero = input(" LOX or Kerosene \n 1: LOX, 2: Kerosene")
        if loxOrKero == '1' :
            volume = 1.5 * (weight / loxWeightPerCubedFoot)
            return format(volume / ((r ** 2) * math.pi), '0.3f')
        elif loxOrKero == '2' :
            volume = 1.5 * (weight / keroseneWeightPerCubedFoot)
            return format(volume / ((r ** 2) * math.pi), '0.3f')

    def volumeInitial():
        F = input("F(" + FU + "):")
        Pc = input("Pc(" + PU + "):")
        At = input("At(" + AU + "):")
        k = float(Pc)*At
        Cf = F/k
        return Cf

    def radius():
        F = input("F(" + FU + "):")
        Cf = input("Cf:")
        At = input("At(" + AU + "):")
        k = float(Cf)*At
        Pc = F/k
        return Pc

    def height():
        F = input("F(" + FU + "):")
        Cf = input("Cf:")
        Pc = input("Pc(" + PU + "):")
        k = float(Cf)*Pc
        At = F/k
        return At

    if(solve == '1'):
        print(heightFromWeightandRadius())
    elif(solve == '2'):
        print(volumeInitial())
    elif(solve == '3'):
        print(radius())
    elif(solve == '4'):
        print(height())
    else :
        print("BAD INPUT GO AWAY REEE")

