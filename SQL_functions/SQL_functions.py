import sqlite3

def create_pdf_table():
    """
    Creates a table to store data extracted from pdfs
    """
    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS PdfTable (
        Serial TEXT,
        CutOffMerit TEXT,
        ChoiceCode TEXT,
        Institute TEXT,
        CourseName TEXT,
        Exam TEXT,
        Type TEXT,
        SeatType TEXT 
        )''')
    conn.commit()
    conn.close()

def create_excel_table():
    '''
    Creates a table to store data extracted from excel worksheets
    '''
    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS ExcelTable (
        Serial TEXT,
        CutOffMerit TEXT,
        ChoiceCode TEXT,
        Institute TEXT,
        CourseName TEXT,
        Exam TEXT,
        Type TEXT,
        SeatType TEXT 
        )''')
    conn.commit()
    conn.close()

def insert_into_table(data_list, table_name):

    '''
    Inserts all data into specified table
    :param data_list: tuple containing all the information corresponding to a row
    :param table_name: name of table to insert data into
    '''

    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    conn.executemany(f'''INSERT INTO {table_name}(CutOffMerit, CutOffScore , ChoiceCode , Institute , CourseName , Exam , Type , SeatType)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_list)
    conn.commit()
    conn.close()

def create_database():
    '''
    Establishes Connection (results in creation of database)
    '''
    conn = sqlite3.connect('database/cutoffdatabase.db')
    conn.close()