import camelot
from SQL_functions import *
import time

t1 = time.perf_counter()
tables = camelot.read_pdf('pdfs/JEE_Main_Cut_off.pdf', pages='all')
all_college_info = []
print('Successfully created PDF object, reading now...\n', flush=True)

for table_num in range(tables.__len__()):
    total_rows = tables[table_num].df.shape[0]
    if table_num == 0:
        for row in range(2, total_rows):
            row_info = tables[table_num].df.iloc[row].to_list()
            OpeningRank = row_info[5].strip('P')
            ClosingRank = row_info[6].strip('P')
            row_info[5] = OpeningRank
            row_info[6] = ClosingRank
            all_college_info.append(tuple(row_info))
            print(f'Finished Row {row} out of {total_rows}', flush=True)

    else:
        for row in range(total_rows):
            row_info = tables[table_num].df.iloc[row].to_list()
            OpeningRank = row_info[5].strip('P')
            ClosingRank = row_info[6].strip('P')
            row_info[5] = OpeningRank
            row_info[6] = ClosingRank
            all_college_info.append(tuple(row_info))
            # print(f'Finished Row {row} out of {total_rows}', flush=True)
    print(f'Finished Table {table_num+1} out of {tables.__len__()}', flush=True)

insert_into_JEEtable(all_college_info, 'JEEPdfTable')
