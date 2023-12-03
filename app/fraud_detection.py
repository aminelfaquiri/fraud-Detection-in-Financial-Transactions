from pyhive import hive
from datetime import datetime
import csv


def fraud_detection(cursor):
    # in the blacklist  :
    in_blacklist_query = """
    SELECT t.*
    FROM transaction_data t
    JOIN blacklist b ON t.merchant_details = b.blacklist_info
    """

    Unusual_Locations_query = """
        SELECT *
        FROM transaction_data
        WHERE location NOT IN ('list', 'of', 'usual', 'locations')
        """

    High_Amounts = """
        SELECT *
        FROM transaction_data
        WHERE amount > (SELECT AVG(amount) * 2 FROM transaction_data)
        """

    Frequent_Transactions = """
        SELECT customer_id, COUNT(*) as transaction_count
        FROM transaction_data
        WHERE date_time BETWEEN 'start_datetime' AND 'end_datetime'
        GROUP BY customer_id
        HAVING transaction_count > threshold
        """ 

    # Execute the Hive query
    cursor.execute(in_blacklist_query)

    # Fetch and print the results :
    result = cursor.fetchall()
    for row in result:
        print(row)

    if len(result) > 0:
        # save the results in a csv file :
        with open('fraud_detect/fraud_detection_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(result)
