import openpyxl
from SQL_functions import *
import time

t1 = time.perf_counter()
wbOb = openpyxl.load_workbook('excelsheets/JEE Main Cut offs-converted.xlsx')
# print(wbOb.sheetnames)
sheet = wbOb['Table 1']
all_college_info = []
for row in range(3, sheet.max_row + 1):
    college_info = []
    for column in range(1, sheet.max_column + 1):
        cell_value = sheet.cell(column=column, row=row).value
        try:
            if column > sheet.max_column - 2:
                college_info.append(int(cell_value))
            else:
                college_info.append(cell_value)
        except ValueError:
            print(cell_value)
            cell_value = cell_value[:-1]
            college_info.append(int(cell_value))

    print(f'Finished row {row} out of {sheet.max_row}')
    all_college_info.append(tuple(college_info))
# for college in all_college_info:
#     print(college)
insert_into_JEEtable(all_college_info, 'JEEExcelTable')