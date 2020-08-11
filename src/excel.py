import xlwt
from xlwt import Workbook
import arial10

wb = Workbook()
used = False


class FitSheetWrapper(object):
    """Try to fit columns to max size of any entry.
    To use, wrap this around a worksheet returned from the 
    workbook's add_sheet method, like follows:

        sheet = FitSheetWrapper(book.add_sheet(sheet_name))

    The worksheet interface remains the same: this is a drop-in wrapper
    for auto-sizing columns.
    """

    def __init__(self, sheet):
        self.sheet = sheet
        self.widths = dict()

    def write(self, r, c, label='', *args, **kwargs):
        self.sheet.write(r, c, label, *args, **kwargs)
        width = arial10.fitwidth(label)
        if width > self.widths.get(c, 0):
            self.widths[c] = width
            self.sheet.col(c).width = width

    def __getattr__(self, attr):
        return getattr(self.sheet, attr)


def sheet(vars, names, eqs, s_name):
    global used
    used = True
    sheet1 = FitSheetWrapper(wb.add_sheet(s_name))

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
