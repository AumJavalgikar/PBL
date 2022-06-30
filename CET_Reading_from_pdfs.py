# This script reads CET cutoff from PDF format and inserts data into sqlite database.

import camelot
from SQL_functions import *
import time


t1 = time.perf_counter()
tables = camelot.read_pdf('pdfs/FE_AI_CAP1.pdf', pages='all')

college_list = []

print('Successfully connected to FE_AI_CAP1.pdf!')

for table_num in range(tables.__len__()):
    total_rows = tables[table_num].df.shape[0]
    for row in range(total_rows):
        row_info = tables[table_num].df.iloc[row].to_list()
        if row_info[0] != 'Sr.No.':
            cutoff = row_info[1]
            cutoff = cutoff.split(' ')
            merit = cutoff[0]
            score = cutoff[1].strip(')').strip('(')
            college_info = [merit, score]
            for element in row_info[2:]:
                element = element.replace('\n', '')
                college_info.append(element)
            college_list.append(tuple(college_info))


insert_into_CETtable(college_list, 'CETPdfTable')
print('Successfully inserted data into database!')
t2 = time.perf_counter()
print('Finished in', t2-t1, 'seconds')
