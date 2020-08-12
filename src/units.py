system = FU = PU = AU = VU = vU = VoU = Mo = ang = aU = MdU = TU = g = DU = pgU = WU = TimeU = None

unstarted = True


def init():
    global unstarted

    def set_units():
        global system, FU, PU, AU, VU, vU, VoU, Mo, ang, MdU, aU, TU, g, DU, pgU, WU, TimeU

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
            VU = 'ft^3/lb'
            VoU = 'ft^3'
            vU = 'ft/sec'
            MdU = 'Lbm/sec'
            TU = '°R'
            Mo = 'lb/mole'
            g = 32.2
            DU = 'in'
            ang = '°'
            aU = 'ft/sec'
            pgU = 'TODO'
            WU = 'Lb'
            TimeU = 'sec'
        else:
            print("Invalid input!\n")
            set_units()

    if unstarted:
        unstarted = False
        set_units()
