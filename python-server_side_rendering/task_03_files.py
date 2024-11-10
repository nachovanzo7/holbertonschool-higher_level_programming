from flask import Flask, request, render_template, jsonify
import json
import csv

app = Flask(__name__)

@app.route('/products')
def get_data():
    source = request.args.get('source')
    item_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source") #ERROR

    data = []

    if source == 'json': #Si es json
        try:
            with open('products.json', 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            return render_template('product_display.html', error="JSON not found")
        except json.JSONDecodeError:
            return render_template('product_display.html', error="ERROR --> JSON File")
        
    elif source == 'csv': #Si es csv
        try:
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV not found")
        except csv.Error:
            return render_template('product_display.html', error="ERROR --> CSV File")

    # Filtrar por 'id' si se proporciona
    if item_id is not None:
        data = [item for item in data if int(item['id']) == item_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    # Renderizar los datos en la plantilla
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
