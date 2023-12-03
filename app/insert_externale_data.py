import requests
from pyhive import hive
from datetime import datetime
from get_api_data import get_data_api
from create_connection import create_connection, close_connection, use_database

cursor, conn = create_connection()
use_database(cursor)

def insert_into_externale(cursor, conn) :

    api_url = 'http://127.0.0.1:5000/api/externalData'
    externalData_data = get_data_api(api_url)

    cursor.execute("DROP TABLE IF EXISTS external_data")


    create_externalData_table_query = """
    CREATE TABLE IF NOT EXISTS external_data (
        customer_id STRING,
        credit_scores INT,
        fraud_reports INT
    ) PARTITIONED BY (day STRING)
    """

    cursor.execute(create_externalData_table_query)
    print("Table external Data is created")

    customer_id = list(externalData_data["credit_scores"])
    credit_scores = list(externalData_data["credit_scores"].values())
    fraud_reports = list(externalData_data["fraud_reports"].values())

    # Insert into :
    insert_external_data_query = """INSERT INTO external_data PARTITION (day=%s) VALUES (%s, %s, %s)"""

    current_day = str(datetime.now().day)

    i = 0
    while True: 

        # if i == len(fraud_reports) :
        if i == 1 :
            break;

        cursor.execute(insert_external_data_query, (
            current_day,
            customer_id[i],
            credit_scores[i],
            fraud_reports[i]
        ))

        print('externale data inserted ',i, '/', len(fraud_reports))
        i +=1

    print("externale data is inserted")
    close_connection(cursor, conn)



insert_into_externale(cursor, conn)