from flask import Flask, render_template, request
import sqlite3
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    
    data = []

    try:
        if source == 'sql': #--> Los datos se sacan de sql
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            rows = cursor.fetchall()
            conn.close()
            for row in rows:
                product = {
                    'id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3]
                }
                data.append(product)

        elif source == 'json': #--> Los datos se sacan de json
            with open('products.json') as file:
                data = json.load(file)

        elif source == 'csv': #--> Los datos se sacan de csv
            with open('products.csv') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]

        else:
            return "Failed: Invalid source did not return status code 200", 400

    except sqlite3.Error as e:
        return "Database error: {}".format(e), 500
    except Exception as e:
        return "Error: {}".format(e), 500

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)