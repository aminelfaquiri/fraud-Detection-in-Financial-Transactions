import requests
from pyhive import hive
from datetime import datetime
from get_api_data import get_data_api
from create_connection import create_connection, close_connection, use_database

cursor, conn = create_connection()
use_database(cursor)

def insert_into_transaction(cursor, conn) :

    api_url = 'http://localhost:5000/api/transactions'
    transaction_data = get_data_api(api_url)

    # Create a table :
    table_name = "transaction_data"

    cursor.execute("DROP TABLE IF EXISTS {table_name}".format(table_name=table_name))

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        amount DOUBLE,
        currency STRING,
        customer_id STRING,
        date_time STRING,
        location STRING,
        merchant_details STRING,
        transaction_id STRING,
        transaction_type STRING
    ) 
    PARTITIONED BY (day STRING)
    """

    cursor.execute(create_table_query)

    print("Table is created")

    # Insert data into the table :
    insert_query = """
    INSERT INTO transaction_data
    PARTITION (day=%s)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    i = 0
    for record in transaction_data[:1]:
        # Calculate hour and day values from date_time
        date_time = datetime.strptime(record['date_time'], '%Y-%m-%dT%H:%M:%S')
        day = date_time.day

        cursor.execute(insert_query, (
            str(day),
            record['amount'],
            str(record['currency']),
            str(record['customer_id']),
            str(record['date_time']),
            str(record['location']),
            str(record['merchant_details']),
            str(record['transaction_id']),
            str(record['transaction_type']),
        ))
        # conn.commit()
        print('transaction inserted ', i, '/', len(transaction_data),datetime.now())
        i += 1
    print("Insertion in transaction_data is done")
    close_connection(cursor, conn)


insert_into_transaction(cursor, conn) 