from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates
from decimal import Decimal
import json
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = "321"
toolbar = DebugToolbarExtension(app)

# Load currencies data
with open("raw_data/currencies.json", "r") as file:
    data = json.load(file)

# Create CurrencyRates object
c = CurrencyRates()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        amount = Decimal(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        # Convert amount
        converted_amount = c.convert(from_currency, to_currency, amount)
        rounded_converted_amount = converted_amount.quantize(Decimal('0.00'))
        formatted_number = format(converted_amount, '.2f')
        if converted_amount < 0.01:
            formatted_number = format(converted_amount, '.4f')
        # Extract symbols for from_currency and to_currency
        for item in data:
            if "cc" in item and item["cc"] == from_currency:
                from_symbol = item["symbol"]
                break
        else:
            from_symbol = None

        for item in data:
            if "cc" in item and item["cc"] == to_currency:
                to_symbol = item["symbol"]
                break
        else:
            to_symbol = None

        # Pass data to template
        return render_template('home.html', amount=amount, from_currency=from_currency, from_symbol=from_symbol, converted_amount=rounded_converted_amount, to_currency=to_currency, to_symbol=to_symbol, formatted_number=formatted_number)
    else: 
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

