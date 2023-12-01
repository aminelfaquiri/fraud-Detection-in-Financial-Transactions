import random
from datetime import datetime, timedelta
import pandas as pd
import json 



def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

def generate_high_frequency_transactions(customer_id, start_date, num_transactions):
    transactions = []
    for _ in range(num_transactions):
        transactions.append({
            "transaction_id": f"T{random.randint(10000, 99999)}",
            "date_time": random_date(start_date, start_date + timedelta(days=1)).isoformat(),
            "amount": random.uniform(10, 1000),
            "currency": random.choice(["USD", "EUR", "GBP"]),
            "merchant_details": f"Merchant{random.randint(1, 20)}",
            "customer_id": customer_id,
            "transaction_type": random.choice(["purchase", "withdrawal"]),
            "location": f"City{random.randint(11, 20)}"  # Different from customer's city
        })
    return transactions

def generate_data(num_transactions, num_customers):
    customers = []
    transactions = []
    merchant_numbers = set()


    merchant_list = list(set([f"Merchant{random.randint(21, 30)}" for _ in range(10)]))
    external_data = {
        "blacklist_info": merchant_list,
        "credit_scores": {},
        "fraud_reports": {}
    }

    for i in range(num_customers):
        customer_id = f"C{i:03}"
        customer_city = f"City{random.randint(1, 10)}"
        customers.append({
            "customer_id": customer_id,
            "account_history": [],
            "demographics": {"age": random.randint(18, 70), "location": customer_city},
            "behavioral_patterns": {"avg_transaction_value": random.uniform(50, 500)}
        })
        external_data["credit_scores"][customer_id] = random.randint(300, 850)
        external_data["fraud_reports"][customer_id] = random.randint(0, 5)

    for i in range(num_transactions):
        customer_id = f"C{random.randint(0, num_customers-1):03}"
        transaction = {
            "transaction_id": f"T{i:05}",
            "date_time": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)).isoformat(),
            "amount": random.uniform(10, 1000) * (10 if random.random() < 0.4 else 1),  # 5% chance of high amount
            "currency": random.choice(["USD", "EUR", "GBP"]),
            "merchant_details": f"Merchant{random.randint(1, 100)}",
            "customer_id": customer_id,
            "transaction_type": random.choice(["purchase", "withdrawal"]),
            "location": f"City{random.randint(1, 10)}"
        }
        transactions.append(transaction)
        for customer in customers:
            if customer["customer_id"] == customer_id:
                customer["account_history"].append(transaction["transaction_id"])
                break

    for customer in random.sample(customers, num_customers // 40):
        transactions.extend(generate_high_frequency_transactions(customer["customer_id"], datetime(2022, 1, 1), 10))

    return transactions, customers, external_data

transactions, customers, external_data = generate_data(1000, 100)


def saveToFile(case,files, data):
    with open(files, 'w') as file:
        if case == 1:
            json.dump(data, file)
        elif case == 2:
            json.dump(data, file)
        elif case == 3:
            json.dump(data, file)

# Example usage:
saveToFile(1,'transactions_data.json', transactions)
saveToFile(2,'customers_data.json', customers)
saveToFile(3,'external_data.json', external_data)