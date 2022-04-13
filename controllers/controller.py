
from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def home():
    return 'Home'

@app.route('/orders')
def index():
    return render_template('index.html', title="Orders", order_list = orders)

@app.route('/orders/<index>')
def display_order(index):
    chosen_order = orders[int(index)]
    return render_template('order.html', title="Order ID", order = chosen_order)