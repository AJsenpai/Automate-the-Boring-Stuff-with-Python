# insert blank rows into spreadsheet
# usage : starting row, number of blank rows , filename

import openpyxl, sys

print(sys.argv[1:])
print(f"c:/Users/Jai/Desktop/Docs/{sys.argv[3]}.xlsx")
wb = openpyxl.load_workbook(f"c:/Users/Jai/Desktop/Docs/{sys.argv[3]}.xlsx")
ws = wb[wb.sheetnames[0]]
ws.insert_rows(int(sys.argv[1]), amount=int(sys.argv[2]))
wb.save(f"c:/Users/Jai/Desktop/Docs/{sys.argv[3]}.xlsx")  # save to see the changes
