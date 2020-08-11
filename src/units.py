system = FU = PU = AU = VU = MdU = TU = g = DU = None


def system():
    global system, FU, PU, AU, VU, MdU, TU, g, DU
    print("1: Metric 2: Imperial\n")
    system = input("What units do you use: ")
    if(system == '1'):
        FU = 'N'
        PU = ''
        AU = ''
        g = 9.81
    elif(system == '2'):
        FU = 'Lbf'
        PU = 'psi'
        AU = 'in^2'
        VU = 'ft/sec'
        MdU = 'Lbm/sec'
        TU = 'R°'
        g = 32.2
        DU = 'in'
    else:
        print("Invalid input:")
