import requests
from pyhive import hive
from datetime import datetime
from decimal import Decimal

def create_connection():
    # Connection parameters :
    host = "localhost"
    port = 10000

    try :
        conn = hive.Connection(host=host, port=port)
        print("Connection to Hive server established successfully!")
    except :
        print("Connection failed")

    # Create a cursor :
    cursor = conn.cursor()

    print("currser initialize")
    return cursor, conn

def use_database(cursor) :
    use_database_query = "USE fraud_detection"
    cursor.execute(use_database_query)
    print("Using the database")

def close_connection(cursor, conn) :
    cursor.close()
    conn.close()
    print("Connection is closed")


create_connection()