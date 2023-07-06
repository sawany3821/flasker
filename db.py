import sqlite3

DATABASE = 'database.db'

def create_firms_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS firms (company_name, earning, future_earning)")
    con.close()
