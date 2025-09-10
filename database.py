import sqlite3

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect("loans.db")
    conn.row_factory = sqlite3.Row
    return conn

# Function to initialize database (run once at startup)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS loan_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            loan_type TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

