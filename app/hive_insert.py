import requests
from pyhive import hive
from thrift import Thrift
import thrift_sasl
from datetime import datetime


########################### create Conection  ########################
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

######################## Create a Database ###########################
database_name = "Fraud_detection"

create_database_query = "CREATE DATABASE IF NOT EXISTS {database_name}".format(database_name=database_name)

cursor.execute(create_database_query)
print("data base is Create ")

# Use the databese :
use_database_query = f"USE {database_name}"
cursor.execute(use_database_query)
print("use the database")

# Hive settings :
# set_dynamic_partition_query = "SET hive.exec.dynamic.partition.mode=nonstrict"
# cursor.execute(set_dynamic_partition_query)
######################################################################
# retrieve data from API :

def get_data_api(api_url) :

    try:
        # Make a GET request :
        response = requests.get(api_url)

        # Check if the request was successful :
        if response.status_code == 200:

            return response.json()

        else:
            # error message if the request was not successful :
            print(f"Error: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        print(f"Error: {e}")

################## insert into Transaction #######################
def insert_into_transaction() : 
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
    insert_query = f"""
    INSERT INTO {table_name}
    PARTITION (day=%s)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    i = 0
    for record in transaction_data :
        # Calculate hour and day values from date_time
        date_time = datetime.strptime(record['date_time'], '%Y-%m-%dT%H:%M:%S')
        day = str(date_time.day)

        cursor.execute(insert_query, (
            record['amount'],
            record['currency'],
            record['customer_id'],
            record['date_time'],
            record['location'],
            record['merchant_details'],
            record['transaction_id'],
            record['transaction_type'],
            day
        ))

        print('transaction inserted ',i, '/', len(transaction_data))
        i +=1

    print("Insertion in transaction_data is done")

insert_into_transaction()

################## insert into Customers #######################
def insert_into_customers() :
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
    for customer in customers_data :
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

# insert_into_customers()

########################## Insert into Externale table ##########################
def insert_into_externale() :

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

        if i == len(fraud_reports) :
            break;

        cursor.execute(insert_external_data_query, (
            current_day,
            customer_id[i],
            credit_scores[i],
            fraud_reports[i]
        ))

        print('customers_data inserted ',i, '/', len(fraud_reports))
        i +=1

    print("externale data is inserted")

# insert_into_externale()

########################## Insert into blacklist table ###########################
def insert_into_blacklist() :
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

    for info in externalData_data["blacklist_info"]:
        cursor.execute(insert_blacklist_query, (info,current_day))

    print("blacklist data is inserted")

# insert_into_blacklist()

#########################################################################
# Commit the changes and close connection :
conn.commit()
cursor.close()
conn.close()