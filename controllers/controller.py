
from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def home():
    return 'Home'

@app.route('/orders')
def index():
    return render_template('index.html', title="Orders", order_list = orders)

@app.route('/orders/<banana>')
def display_order(banana):
    chosen_order = orders[int(banana)]
    return render_template('order.html', title="Order ID", order = chosen_order)