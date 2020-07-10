#Calculate combustion chamber parameters, with values given
# F = Cf*Pc*At
import numpy as np

print("1: Metric 2: Imperial")
units = input("What units do you use:")
if(units == 1):
    FU = 'N' 
    PU = ''
    AU = ''
elif(units == 2):
    FU = 'Lbf' 
    PU = 'psi' 
    Au = 'in^2'
else: units = input("Invalid input:")

print("1: F(thrust) \n 2: Cf (Coefficient of thrust) \n 3: Pc(Chamber Pressure) \n 4: At (Throat area)")
solve = input("What are you solving for?")



def thrust():
    Cf = input("Cf:")
    Pc = input("Pc:")
    At = input("At:")
    F = Cf*Pc*At
    return F

def coefficient():
    F = input("F:")
    Pc = input("Pc:")
    At = input("At:")
    k = float(Pc)*At
    Cf = F/k
    return Cf

def pressure():
    F = input("F:")
    Cf = input("Cf:")
    At = input("At:")
    k = float(Cf)*At
    Pc = F/k
    return Pc

def throat():
    F = input("F:")
    Cf = input("Cf:")
    Pc = input("Pc:")
    k = float(Cf)*Pc
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

