import requests
from pyhive import hive
from datetime import datetime
from get_api_data import get_data_api
from create_connection import create_connection, close_connection, use_database

cursor, conn = create_connection()
use_database(cursor)

def insert_into_customers(cursor, conn) :
    api_url = 'http://127.0.0.1:5000/api/customers'
    customers_data = get_data_api(api_url)

    cursor.execute("DROP TABLE IF EXISTS customers_data")

    create_customers_table_query = """
    CREATE TABLE IF NOT EXISTS customers_data (
        customer_id STRING,
        account_history STRING,
        avg_transaction_value DOUBLE,
        age INT,
        location STRING
    ) PARTITIONED BY (day STRING)
    """

    print("Table customer is created")
    cursor.execute(create_customers_table_query)

    # Insert into :
    insert_customers_query = """
    INSERT INTO customers_data PARTITION (day=%s)
    VALUES (%s, %s, %s, %s, %s)
    """
    i = 0
    for customer in customers_data[:1] :
        account_history = ' '.join(customer['account_history'])
        print(str(account_history))
        current_day = str(datetime.now().day)

        cursor.execute(insert_customers_query, (
            current_day,
            customer['customer_id'],
            str(account_history),
            customer['behavioral_patterns']['avg_transaction_value'],
            customer['demographics']['age'],
            customer['demographics']['location']
        ))
        print('customers_data inserted ',i, '/', len(customers_data))
        i +=1

    print("data in table customer is inserted")
    close_connection(cursor, conn)



insert_into_customers(cursor, conn)