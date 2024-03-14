import sqlite3
from datetime import datetime
import calendar

def get_all_requests(db_name = "", table = "", model_type= ""):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    if model_type == "verification":
        cursor.execute(f"SELECT * FROM {table}")
        users = cursor.fetchall()
        connection.close()
        return users


    cursor.execute(f"SELECT * FROM {table} WHERE model = '{model_type}'")

    users = cursor.fetchall()

    connection.close()
    
    return users

def get_requests_by_month(db_name = "", table = "", model_type= "", year="", month=""):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    start_date = f"{year}-{str(month).zfill(2)}-01 00:00:00"
    end_date = f"{year}-{str(int(month) + 1).zfill(2)}-01 00:00:00"

    if model_type == "verification":
        query = f"SELECT * FROM {table} WHERE date >= ? AND date < ?"
        cursor.execute(query, (start_date, end_date))

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

    query = f"SELECT * FROM {table} WHERE date >= ? AND date < ? AND model = ?"
    cursor.execute(query, (start_date, end_date, model_type))

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows



def get_requests_by_month_limit(db_name = "", table = "", model_type= "", year="", month="", limit = ""):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    start_date = f"{year}-{str(month).zfill(2)}-01 00:00:00"
    end_date = f"{year}-{str(int(month) + 1).zfill(2)}-01 00:00:00"

    if model_type == "verification":
        query = f"SELECT * FROM {table} WHERE date >= ? AND date < ? LIMIT ?"
        cursor.execute(query, (start_date, end_date, limit))

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

    query = f"SELECT * FROM {table} WHERE date >= ? AND date < ? AND model = ? LIMIT ?"
    cursor.execute(query, (start_date, end_date, model_type, limit))

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows