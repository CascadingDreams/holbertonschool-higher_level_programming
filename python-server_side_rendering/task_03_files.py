
'''Simple flask app that renders html using a jinga template'''

from flask import Flask, request, render_template, jsonify
import json
import csv

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
    print("=== DEBUG: Products route called ===")
    source = request.args.get('source')
    item_id = request.args.get('id')
    print(f"DEBUG: source parameter = '{source}'")
    print(f"DEBUG: item_id parameter = '{item_id}'")
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                               products=[],
                               error_message="Wrong source")
        
    print(f"DEBUG: Source validation passed, source = '{source}'")
    
    # if source is json then....     
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    products = data
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
        print("DEBUG: Entering CSV branch")
        try:
            print("DEBUG: Attempting to open product.csv")
            with open('product.csv', mode='r') as f:
                print("DEBUG: File opened successfully")
                reader = csv.DictReader(f)
                print("DEBUG: CSV reader created")
                products = list(reader)
                print(f"Type of data: {type(products)}")
                print(f"Data content: {products}")
        except FileNotFoundError:
            return render_template('product_display.html',
                                   products=[],
                                   error_message="Could not load CSV data")
            
    #item_id logic - should be int and found
    if item_id:
        try:
            id_value = int(item_id)
            filtered_products = []
            
            for p in products:
                try:
                    product_id = int(p.get('id', 0))
                    if product_id == id_value:
                        filtered_products.append(p)
                except (ValueError, TypeError):
                    # Skip products with invalid ID values
                    continue
                    
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)