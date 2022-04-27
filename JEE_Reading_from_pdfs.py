import camelot
from SQL_functions import *
import psutil
import time


t1 = time.perf_counter()
tables = camelot.read_pdf('pdfs/JEE_Main_Cut_off.pdf', pages='1-2')
college_list = []

# print(tables[0].df.iloc[0].to_list())
# print(tables[0].df.iloc[1].to_list())
# print(tables[0].dc.iloc[2].to_list())

for table_num in range(3, tables.__len__()):
    total_rows = tables[table_num].df.shape[0]
    for row in range(total_rows+1):
        row_info = tables[table_num].df.iloc[row].to_list()
        # print(tables[table_num].df.iloc[row].to_list())
        if row_info[0] != 'Sr.No.':
            cutoff = row_info[1]
            cutoff = cutoff.split(' ')
            merit = cutoff[0]
            score = cutoff[1].strip(')').strip('(')
            college_info = [merit, score]
            for element in row_info[2:]:
                # element = regex.sub(element, '\w+')
                element = element.replace('\n', '')
                college_info.append(element)
            # print(college_info)
            college_list.append(tuple(college_info))