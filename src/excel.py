import xlwt
from xlwt import Workbook

wb = Workbook()


def sheet(vars, names, eqs, s_name):
    sheet1 = wb.add_sheet(s_name)

    style = xlwt.easyxf('font: bold 1')

    sheet1.write(0, 0, 'Variables', style)
    sheet1.write(0, 1, 'Values', style)
    sheet1.write(0, 2, 'Method', style)

    for y in range(0, len(names)):
        sheet1.write((y+1), 0, names[y])
    for x in range(0, len(vars)):
        sheet1.write((x+1), 1, vars[x])
    for z in range(0, len(eqs)):
        sheet1.write((z+1), 2, eqs[z])


def pretty(strs):
    for x in strs:
        x.replace('**', '^')
        x.replace('np.', '')

    return strs
