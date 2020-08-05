#Calculate apogee from mass, thrust and other fun things
import math
import numpy

def run():
    print("\nWelcome to the Apogee Calculator! \n")
    print("Here you can find the apogee given dry mass, propellant/oxidizer combined mass and thrust, the optimal dry mass for a given apogee, or the optimal thrust numbers for a mass and burn time \n")
    print(apogee())

def apogee():
    #Please note, the reason the units are asked for in imperial is because that is what is more commonly used by us, however these must be converted to metric in the codebase.
    #AS FOLLOWS IS METRIC. DOTH NOT BE FOOLED!
    m = float(input("Dry mass in lbs : ")) * 0.453592
    M = float(input("total rocket + propellant + oxidizer mass in lbs : ")) * 0.453592
    t = float(input("Burn time in seconds : "))
    T = float(input("Thrust in lbf : ")) * 4.44822
    A = float(input("Frontal area of rocket in square inches : ")) * 0.00064516
    Cd = float(input("Drag Coefficient (if you don't know, 0.5 is a good estimate) : "))
    originalm = m
    m = m + (M-m) / 2
    mg = m * 9.8
    Mg = M * 9.8
    rho = (1.112 + 0.1948) / 2
    k = 0.5 * rho * Cd * A
    q = math.sqrt((T-Mg)/k)
    x = (2 * k * q ) / M
    #math.exp IS DENOTATION FOR e^x
    v = q * (1 - math.exp(-1 * x * t ) / (1 + math.exp(-1 * x * t )))
    y1 = ((-1 * m) / (2 * k )) * numpy.log((T - mg - k * v ** 2) / (T - mg))
    yc = (originalm / (2 * k)) * (numpy.log((originalm * 9.8 + k * v ** 2) / (originalm * 9.8)))
    altitude = (y1 + yc) * 3.28084
    qa = math.sqrt((originalm * 9.8) / k)
    qb = math.sqrt(9.8 * k / m )
    ta = math.atan(v / qa) / qb
    return format(altitude, '0.3f') + " feet coasting time of " + format(ta, '0.3f') + " seconds and a velocity of mach " + format(v * 0.00291545, '0.3f')

