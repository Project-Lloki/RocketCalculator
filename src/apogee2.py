import math
import numpy as np
import restart as r
import units as u
import excel as e
from src.apogeeFiles.burn import burn
from src.apogeeFiles.coast import coast
from apogeeFiles.descent import descent


def run():
    print("\nWelcome to the Apogee Calculator! \n")
    print("Here you can find the apogee given dry mass, propellant/oxidizer combined mass and thrust, the optimal dry mass for a given apogee, or the optimal thrust numbers for a mass and burn time \n")

    # Please note, the reason the units are asked for in imperial is because that is what is more commonly used by us, however these must be converted to metric in the codebase.
    # AS FOLLOWS IS METRIC. DOTH NOT BE FOOLED!

    mf = float(input("Dry mass in lbs : ")) #* 0.453592
    m0 = float(input("total rocket including propellant in lbs : ")) #* 0.453592
    tburn = float(input("Burn time in seconds : "))
    Thrust = float(input("Thrust in lbf : ")) * 4.44822
    isp = float(input("Specific impulse : "))
    FArea = float(input("Frontal area of rocket in square inches : ")) * 0.00064516
    Cd = float(input("Drag Coefficient (if you don't know, 0.5 is a good estimate for subsonic, 0.6 for transonic/supersonic) : "))
    launchAngle = float(input("Launch angle from horizontal : "))
    #VACUUM SETUP

    burn.run()
    coast.run()
    descent.run()

    propellantMass = m0-mf
    F = isp * propellantMass/tburn
    g0 = -9.81
    Burnoutgf = 9.8787
    c = g0 * isp
    burnoutv = c * np.log(m0/mf)
    #in meters / second
    averageBurnGravity = (g0 + Burnoutgf)/2


    burnoutalt = burnoutv / 2 * tburn
    apogeealt = burnoutalt + burnoutv**2 / (-2*g0)
    burnacceleration = burnoutv / tburn

    #h = 0.5(v^2)/g

    #the thing about burnout is that the derivative of acceleration is at its maximum so we can (but do not have to, theres an easier way) visualize the
    #derivative of the rockets acceleration as going to be at its maximum point to be at burnout which then leaves us with in this drag ignored scenario with an acceleration
    #addition of gravity.

    coastingtime = -1* burnoutv / g0
    #recoverytime =math.sqrt(-2*g0*apogeealt)/(-1*g0)
    #meters
    print(format(F, '0.3f') + "THRUST IN LBS!")
    print(format(apogeealt, '0.3f') + " meters and a coasting time of " + format(coastingtime, '0.3f') + " seconds and a max velocity of " + format(burnoutv, '0.3f') + "m/s")
    print(format(burnoutalt, '0.3f'))
    #print(format(recoverytime, '0.3f'))
    # one quicek note about burnout is that the acceleration stops increasing and begins to decrease, this means that the derivative of acceleration is zero.
    # using kinematics equation v0^2 = v^2 + 2adeltax
    # boils down to in this case -burnoutv/2g = deltax
    #C IS METRIC

    r.restart()
