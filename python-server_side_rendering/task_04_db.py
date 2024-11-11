from flask import Flask, render_template, request
import sqlite3
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    data = []

    try:
        if source == 'sql':  # Los datos se sacan de SQL
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            # Filtramos por ID si se especifica un producto específico
            if product_id:
                cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            else:
                cursor.execute('SELECT * FROM Products')
                
            rows = cursor.fetchall()
            conn.close()
            
            if not rows:
                return render_template('product_display.html', error="Product not found"), 200

            for row in rows:
                product = {
                    'id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3]
                }
                data.append(product)

        elif source == 'json':  # Los datos se sacan de JSON
            with open('products.json') as file:
                data = json.load(file)
                # Filtramos por ID si se especifica
                if product_id:
                    data = [product for product in data if str(product['id']) == product_id]
                    if not data:
                        return render_template('product_display.html', error="Product not found"), 200

        elif source == 'csv':  # Los datos se sacan de CSV
            with open('products.csv') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]

                if product_id: #si se especifica --> x id
                    data = [product for product in data if product['id'] == product_id]
                    
                    if not data: #--> no se encontró producto
                        return render_template('product_display.html', error="Product not found"), 200 

        else:
            return render_template('product_display.html', error="Wrong source"), 200

    except sqlite3.Error as e:
        return render_template('product_display.html', error="Database error: {}".format(e)), 500
    except Exception as e:
        return render_template('product_display.html', error="Error: {}".format(e)), 500

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
