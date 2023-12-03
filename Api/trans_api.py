from flask import Flask,jsonify
import json


app = Flask(__name__)

# read data from json file :
def read_json_file(filename) :
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

transactions = read_json_file("Api/Data_json/transactions_data.json")
customers = read_json_file("Api/Data_json/customers_data.json")
external_data = read_json_file("Api/Data_json/external_data.json")

# create app route :
@app.route('/api/transactions')
def transactions_data():
    return jsonify(transactions)

@app.route('/api/customers')
def customers_data():
    return jsonify(customers)

@app.route('/api/externalData')
def externalData():
    return jsonify(external_data)

# error handling :
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

# Run the server :
if __name__ == '__main__':
    app.run(debug=True)
