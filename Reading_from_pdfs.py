import camelot
from SQL_functions import *


tables = camelot.read_pdf('pdfs/FE_AI_CAP1.pdf', pages='all')

count = 0
college_list = []


for table_num in range(tables.__len__()):
    total_tables = tables[table_num].df.shape[0]
    for row in range(total_tables):
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
# print(count)
for college in college_list:
    print(college)

insert_into_table(college_list, 'PdfTable')
# print(tables[0].df.iloc[0])