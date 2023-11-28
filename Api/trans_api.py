from flask import Flask,jsonify
from data_generator import generate_data


app = Flask(__name__)

transactions, customers, external_data = generate_data(1000, 100)


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
