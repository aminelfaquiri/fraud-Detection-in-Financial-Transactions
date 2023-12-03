import requests
from pyhive import hive
from datetime import datetime
from get_api_data import get_data_api
from create_connection import create_connection, close_connection, use_database

cursor, conn = create_connection()
use_database(cursor)

def insert_into_blacklist(cursor, conn):
    api_url = 'http://127.0.0.1:5000/api/externalData'
    externalData_data = get_data_api(api_url)

    cursor.execute("DROP TABLE IF EXISTS blacklist")


    create_blacklist_table_query = """
    CREATE TABLE IF NOT EXISTS blacklist (
        blacklist_info STRING
    ) PARTITIONED BY (day STRING)
    """

    cursor.execute(create_blacklist_table_query)
    print("Table blacklist Data is created")

    current_day = str(datetime.now().day)

    # Insert data into the blacklist_info table using a loop
    insert_blacklist_query = "INSERT INTO blacklist PARTITION (day=%s) VALUES (%s)"

    for info in externalData_data["blacklist_info"][:1]:
        cursor.execute(insert_blacklist_query, (info,current_day))

    print("blacklist data is inserted")
    close_connection(cursor, conn)



insert_into_blacklist(cursor, conn)