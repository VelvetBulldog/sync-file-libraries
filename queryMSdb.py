
import pyodbc

def MSSQLdict():

    con = pyodbc.connect('DRIVER={SQL Server};SERVER=AUSSQL03\\BI;DATABASE=ETL-REPOSITORY;UID=python;PWD=K1ll3RPyth0n')
    cur = con.cursor()

    querystring = "select etl_file_name, etl_file_path from etl_file_input where etl_file_id not in (192,212,236,248,252,256,1213,320,324) and isEnabled = 1"
    cur.execute(querystring)

    my_dict = {}
    for row in cur.fetchall():
        tup = row
        my_dict[tup[0].upper() + ".TXT"] = tup[1]
    con.commit()

    return my_dict