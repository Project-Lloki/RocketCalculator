import math
import numpy as np
import restart as r
import units as u
import excel as e


def run():
    print("\nWelcome to the Apogee Calculator! \n")
    print("Here you can find the apogee given dry mass, propellant/oxidizer combined mass and thrust, the optimal dry mass for a given apogee, or the optimal thrust numbers for a mass and burn time \n")

    # Please note, the reason the units are asked for in imperial is because that is what is more commonly used by us, however these must be converted to metric in the codebase.
    # AS FOLLOWS IS METRIC. DOTH NOT BE FOOLED!

    m0 = float(input("Dry mass in lbs : ")) * 0.453592
    mf = float(input("total rocket including propellant in lbs : ")) * 0.453592
    tburn = float(input("Burn time in seconds : "))
    Thrust = float(input("Thrust in lbf : ")) * 4.44822
    isp = float(input("Specific impulse : "))
    FArea = float(input("Frontal area of rocket in square inches : ")) * 0.00064516
    Cd = float(input("Drag Coefficient (if you don't know, 0.5 is a good estimate for subsonic, 0.6 for transonic/supersonic) : "))
    launchAngle = float(input("Launch angle from horizontal : "))
    #VACUUM SETUP
    g0 = -9.81
    c = g0 * isp
    burnoutv = c * np.log(m0/mf)
    #in meters / second

    burnoutalt = burnoutv / 2 * tburn
    apogeealt = burnoutalt + (burnoutv/(2*g0))
    coastingtime = -1* burnoutv / g0
    #meters
    print(format(apogeealt, '0.3f') + "meters and a coasting time of " + format(coastingtime, '0.3f') + "and a max velocity of " + format(burnoutv, '0.3f') + "m/s")
    # using kinematics equation v0^2 = v^2 + 2adeltax
    # boils down to in this case -burnoutv/2g = deltax
    #C IS METRIC

    r.restart()
