from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Customer, Order
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db.init_app(app)


@app.route('/', methods=['GET'])
def root():
    return jsonify({"hello": "world"})


@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.as_dict() for customer in customers])

@app.route('/customer/<id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    if customer:
        return jsonify(customer.as_dict())
    else:
        return jsonify({"error": "Customer not found"}), 404

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.as_dict() for order in orders])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))