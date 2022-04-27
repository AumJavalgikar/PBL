import sqlite3

def add_to_main_table():
    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS MainTable(
    Serial PRIMARY KEY,
    
    )''')
def create_main_table():
    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    column_names = conn.execute('''SELECT * FROM table1 
    ''')
    column_names = column_names.fetchall()[0]
    print(column_names)
    column_names = list(column_names)
    column_names[0] = 'Serial'
    column_names[1] = 'Cut Off Merit'
    column_names[5] = 'Exam (JEE/MHT-CET)'
    column_names=tuple(column_names)
    print(column_names)
    column1, column2, column3, column4, column5, column6, column7, column8 = column_names
    conn.execute('''CREATE TABLE IF NOT EXISTS MainTable (
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

def fetch_scores():
    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    results = conn.execute('''SELECT * FROM MainTable   
    ''')
    results=results.fetchall()
    conn.close()
    return results

def insert_into_MainTable1(data_list):
    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    conn.executemany('''INSERT INTO MainTable1(CutOffMerit, CutOffScore , ChoiceCode , Institute , CourseName , Exam , Type , SeatType)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_list)
    conn.commit()
    conn.close()

def insert_into_table(data_list, table_name):
    conn = sqlite3.connect('pdfs/cutoffdatabase.db')
    conn.executemany(f'''INSERT INTO {table_name}(CutOffMerit, CutOffScore , ChoiceCode , Institute , CourseName , Exam , Type , SeatType)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_list)
    conn.commit()
    conn.close()

def create_database():
    conn = sqlite3.connect('database/database.db')
    conn.close()