import psycopg2
from config import *


def insert_data(value):
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASS)
    except ConnectionError:
        return print("Unable to connect to database")

    cur = conn.cursor()
    sql = "INSERT INTO temperature (temp) VALUES (" + value + ");"
    try:
        cur.execute(TABLE, conn)
        cur.execute(sql, conn)
    except:
        print("Query failed")

    cur.close()
    conn.close()
    conn = None
    cur = None
    return "Success"

