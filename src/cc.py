#Calculate combustion chamber parameters, with values given
# F = Cf*Pc*At

def run():
    print("\nWelcome to the Combustion Chamber Calculator! \n")
    print("Here you can find thrust (F), coefficient of thrust (Cf), Chamber Pressure (Pc) or Throat Area (At) when you know at least three of these values.\n")
    print("1: Metric 2: Imperial\n")
    units = input("What units do you use:\n")
    if(units == '1'):
        FU = 'N' 
        PU = ''
        AU = ''
    elif(units == '2'):
        FU = 'Lbf' 
        PU = 'psi' 
        AU = 'in^2'
    else: units = input("Invalid input:")

    print("\nChoose the value you wish to calculate for:")
    print("\n 1: F(thrust) \n 2: Cf (Coefficient of thrust) \n 3: Pc(Chamber Pressure) \n 4: At (Throat area)\n")
    solve = input("What are you solving for?")



    def thrust():
        Cf = float(input("Cf:"))
        Pc = float(input("Pc (" + PU + "):"))
        At = float(input("At(" + AU + "):"))
        F = Cf*Pc*At
        return F

    def coefficient():
        F = float(input("F(" + FU + "):"))
        Pc = float(input("Pc (" + PU + "):"))
        At = float(input("At(" + AU + "):"))
        k = Pc*At
        Cf = F/k
        return Cf

    def pressure():
        F = float(input("F(" + FU + "):"))
        Cf = float(input("Cf:"))
        At = float(input("At(" + AU + "):"))
        k = Cf*At
        Pc = F/k
        return Pc

    def throat():
        F = float(input("F(" + FU + "):"))
        Cf = float(input("Cf:"))
        Pc = float(input("Pc (" + PU + "):"))
        k = Cf*Pc
        At = F/k
        return At

    if(solve == 1):
        print(thrust())
    elif(solve == 2):
        print(coefficient())
    elif(solve == 3):
        print(pressure())
    elif(solve == 4):
        print(throat())

