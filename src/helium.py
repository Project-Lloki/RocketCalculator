import matplotlib.pyplot as plt

pressures4 = []
volumes2 = []
data = [[], [], [], []]
for x in range(100, 2000):
    p2 = 350
    v2 = 445 + 622.6 + x
    v1 = x
    p1 = (v2*p2)/v1
    volumes2.append(v2)
for x in range(100, 2000):
    p3 = 350
    v3 = volumes2[x-100]
    v4 = v3 + 1846.4
    p4 = (v3*p3)/v4
    pressures4.append(p4)
    # data.append([p3, v3, p4, v4])
pressures = pressures4
pressures.sort()
print(data)
print(pressures[1698-101])
print(pressures4.index(pressures[1698-101]))


# volume in the tanks

graphType = input('Burntime or Volume (b/v): ')
# lox lb/in^3 = 0.04122123703202348
# Kero lb/in^3 = 0.0289351842067375
if graphType == 'b':
    b = []
    p = []
    for x in range(0, 1846):
        p3 = 350
        v3 = 1214 + 84.9 + 60.7
        v4 = v3 + x
        p4 = (v3*p3)/v4
        changeInLox = (6.52-(6.52/3.2))*0.04122123703202348
        changeInFuel = (6.52/3.2)*0.0289351842067375
        adjustedFlow = changeInFuel+changeInLox
        burntime = x/adjustedFlow
        b.append(burntime)
        p.append(p4)
    # plotting the points
    plt.plot(b, p)

    # naming the x axis
    plt.xlabel('burntime')
    # naming the y axis
    plt.ylabel('pressure in the tanks')

    # giving a title to my graph
    plt.title('P v T')

    # function to show the plot
    plt.show()
else:
    v = []
    p = []
    for x in range(0, 2766):
        p3 = 350
        v3 = 2300 + (1214*0.1) + (1698*.1)
        v4 = v3 + x
        p4 = (v3*p3)/v4
        v5 = v3 + 2766
        v.append(v5-x)
        p.append(p4)

    # plotting the points
    plt.plot(v, p)

    # naming the x axis
    plt.xlabel('ullage volume')
    # naming the y axis
    plt.ylabel('pressure in the tanks')

    # giving a title to my graph
    plt.title('P v V')

    # function to show the plot
    plt.show()
