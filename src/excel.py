import xlwt
from xlwt import Workbook

wb = Workbook()
used = False


def sheet(vars, names, units, eqs, s_name):
    global used
    used = True
    sheet1 = wb.add_sheet(s_name)

    style = xlwt.easyxf('font: bold 1')

    sheet1.write(0, 0, 'Variables', style)
    sheet1.write(0, 1, 'Values', style)
    sheet1.write(0, 2, 'Units', style)
    sheet1.write(0, 3, 'Method', style)

    for y in range(0, len(names)):
        sheet1.write((y+1), 0, names[y])
    for x in range(0, len(vars)):
        sheet1.write((x+1), 1, vars[x])
    for w in range(0, len(units)):
        sheet1.write((w+1), 2, units[w])
    for z in range(0, len(eqs)):
        sheet1.write((z+1), 3, eqs[z])


def pretty(strs):
    new = []

    for x in strs:
        x = x.replace('**', '^')
        x = x.replace('np.', '')
        new.append(x)

    return new
