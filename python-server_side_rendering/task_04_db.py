
'''Simple flask app that renders html using a jinga template'''

from flask import Flask, request, render_template, jsonify
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open ('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []    
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    item_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                               products=[],
                               error_message="Wrong source")
    
    # if source is json then....     
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    products = data
                    print(f"DEBUG: products:{products}")
                elif isinstance(data, dict):
                    products = data.get('products', [])
                else:
                    products = []
        except (FileNotFoundError, json.JSONDecodeError):
            return render_template('product_display.html',
                                   products=[],
                                   error_message="Could not load JSON data")
    
    # if source is csv
    elif source == 'csv':
        try:
            with open('products.csv', mode='r') as f:
                reader = csv.DictReader(f)
                products = list(reader)
                print(f"DEBUG: products:{products}")
        except FileNotFoundError:
            return render_template('product_display.html',
                                   products=[],
                                   error_message="Could not load CSV data")
            
    # if source in sql
    elif source == 'sql':
        print("DEBUG: Entering SQL branch")
        products = read_sql_data()
        if not products and products is not None:
            pass
        
        #item_id logic - should be int and found
    if item_id:
        try:
            # Convert user input to integer once
            target_id = int(item_id)
            
            # Use list comprehension with safe ID conversion
            def safe_get_id(product):
                try:
                    return int(product.get('id', 0))
                except (ValueError, TypeError):
                    return None
            
            # Filter products in one clean expression
            filtered_products = [p for p in products if safe_get_id(p) == target_id]
            
            if not filtered_products:
                return render_template('product_display.html',
                                    products=[],
                                    error_message="Product not found")
            
            products = filtered_products
            
        except ValueError:
            return render_template('product_display.html',
                                products=[],
                                error_message="Invalid ID format")

    return render_template('product_display.html', 
                        products=products, 
                        error_message=None)
            
def read_sql_data():
    try:
        with sqlite3.connect('products.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
        
            rows = cursor.fetchall()
            
            products = [dict(row) for row in rows]
            
            print(f"DEBUG: Successfully read {len(products)} products from database")
            return products
            
    except sqlite3.Error as e:
        print(f"DEBUG: Database error occurred: {e}")
        return []
    
    except Exception as e:
        print(f"DEBUG: Unexpected error reading database: {e}")
        return []  

if __name__ == '__main__':
    app.run(debug=True, port=5000)