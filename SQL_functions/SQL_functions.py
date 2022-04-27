import sqlite3


def create_JEE_pdf_table():
    """
       Creates a table to store data extracted from pdfs containing JEE Mains Cutoffs
       """
    conn = sqlite3.connect('database/cutoffdatabase.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS CETPdfTable (
           Serial INTEGER PRIMARY KEY,
           Institute TEXT,
           AcademicProgramName TEXT,
           Quota TEXT,
           SeatType TEXT,
           Gender TEXT,
           OpeningRank INTEGER,
           ClosingRank INTEGER
           )''')
    conn.commit()
    conn.close()


def create_CET_pdf_table():
    """
    Creates a table to store data extracted from pdfs containing CET AI Cutoffs
    """
    conn = sqlite3.connect('database/cutoffdatabase.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS CETPdfTable (
        Serial INTEGER PRIMARY KEY,
        CutOffMerit INTEGER,
        CutOffScore INTEGER,
        ChoiceCode TEXT,
        Institute TEXT,
        CourseName TEXT,
        Exam TEXT,
        Type TEXT,
        SeatType TEXT 
        )''')
    conn.commit()
    conn.close()


def create_CET_excel_table():
    """
    Creates a table to store data extracted from excel worksheets containing JEE Mains cutoffs
    """
    conn = sqlite3.connect('database/cutoffdatabase.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS CETExcelTable (
        Serial INTEGER PRIMARY KEY,
        CutOffMerit INTEGER,
        CutOffScore INTEGER,
        ChoiceCode TEXT,
        Institute TEXT,
        CourseName TEXT,
        Exam TEXT,
        Type TEXT,
        SeatType TEXT 
        )''')
    conn.commit()
    conn.close()


def insert_into_CETtable(data_list, table_name):
    """
    Inserts all data into specified table containing CET AI cutoffs
    :param data_list: **list** containing **tuples** containing all the information corresponding to a row
    :param table_name: name of table to insert data into
    """

    conn = sqlite3.connect('database/cutoffdatabase.db')
    conn.executemany(f'''INSERT INTO {table_name}(CutOffMerit, CutOffScore , ChoiceCode , Institute , CourseName , Exam , Type , SeatType)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_list)
    conn.commit()
    conn.close()

def insert_into_JEEtable(data_list, table_name):
    """
    Inserts all data into specified table containing JEE Mains cutoffs
    :param data_list: **list** containing **tuples** containing all the information corresponding to a row
    :param table_name: name of table to insert data into
    """

    conn = sqlite3.connect('database/cutoffdatabase.db')
    conn.executemany(f'''INSERT INTO {table_name}(Institute, AcademicProgramName, Quota, SeatType, Gender, OpeningRank, ClosingRank)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_list)
    conn.commit()
    conn.close()

def create_database():
    """
    Establishes Connection (results in creation of database)
    """
    conn = sqlite3.connect('database/cutoffdatabase.db')
    conn.close()
