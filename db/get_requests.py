import sqlite3

def get_all_requests(db_name = "", table = ""):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM {table}')
    users = cursor.fetchall()

    connection.close()
    
    return users
