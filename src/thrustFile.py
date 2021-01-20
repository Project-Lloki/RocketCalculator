#generate
import sys
import math
import scipy.integrate as integrate
def run():

    sys.stdout = open('sparkyLatest.rse', 'w')
    propMassGrams = float(input("Propellant weight in lbs: ")) * 453.592
    burnTime = float(input("Burn time in seconds: "))
    totalEngineMassGrams = float(input("Total mass of engine including tanks and plumbing, your 'motor' in lbs: " )) * 453.592
    massFrac = propMassGrams/totalEngineMassGrams * 100
    diameter = float(input("Diameter of rocket in inches: ")) * 25.4
    length = float(input("Length from tip of helium tank to nozzle in inches: ")) * 25.4
    initialMdot = float(input("Initial Mdot in lbm/s: "))
    initialTankPressure = float(input("Initial Tank pressure in psi: "))
    finalTankPressure = float(input("Final Tank pressure in psi: "))
    AltitudeEstimates = [100, 300, 500, 1000, 1700, 2500, 3500, 4850, 6250, 7900, 9600, 11500, 14000, 18500]
    # 15 second burn extimated altitude temporary only.
    print("<engine-database><engine-list><engine  mfg=\"Mckinney High School\" code=\"001\" Type=\"Liquid Kerolox\" dia=\""+format(diameter)+"\" len=\""+format(length)+"\" initWt=\""+format(totalEngineMassGrams)+"\""
          + "propWt=\"" + format(propMassGrams) + "\" delays=\"1\" auto-calc-mass=\"1\" auto-calc-cg=\"1\"" +
"avgThrust=\"6700\" peakThrust=\"7330\" throatDia=\"101.6\" exitDia=\"5\" Itot=\"18.017\""+
"burn-time=\""+ format(burnTime) + "\" massFrac=\"" + format(massFrac) +  "\" Isp=\"240\" tDiv=\"10\" tStep=\"-1.\" tFix=\"1\""+
"FDiv=\"10\" FStep=\"-1.\" FFix=\"1\" mDiv=\"10\" mStep=\"-1.\" mFix=\"1\" cgDiv=\"10\""+
"cgStep=\"-1.\" cgFix=\"1\"> <comments>The sparky engine custom liquid fueled engine 1500lbf@sea level for 15 seconds. - Ismail Hozain</comments> <data>")
    mdot = 0
    currentThrust = 0
    mdotSpent = 0
    # TAKE THIS INTEGRAL OF THE MDOT EQUATION TO FIND THE TOTAL PROPELLANT MASS SPENT.
    def f(t):
        return initialMdot * math.sqrt((initialTankPressure-(finalTankPressure/burnTime) * t/initialTankPressure))

    propMassGrams = integrate.quad(f, 0, burnTime) * 453.592
    print(propMassGrams)
    #currentPropellantMass = propMassGrams - mdot
    #dryMass = totalEngineMassGrams - propMassGrams
    #mdot = initialMdot*sqrt((initialTankPressure-(finalTankPressure/burnTime)*t)/initialTankPressure)
    #for t in range (1, 15):
     #   mdot = initialMdot * math.sqrt((initialTankPressure - (finalTankPressure/burnTime) * t) / initialTankPressure)
      #  currentPropellantMass -= mdot
       # currentThrust = 4.48 * (-0.02474 * AltitudeEstimates[t] + 1517.89)

        #print("<eng-data t=" + format(t)+"\" f=\"" + format(currentThrust) + "\" m=\"" + format(currentPropellantMass+dryMass)+ "\" cg=\"1524\"/>")
#       y = -0.02474x + 1517.89 is the linear reg for thrust. 4.48 is the conversion factor from lbf to n.
    #print("</data></engine></engine-list></engine-database>")
#      <eng-data  t=\"1\" f=\"6740.6\" m=\"68038.9\" cg=\"1524.\"/>