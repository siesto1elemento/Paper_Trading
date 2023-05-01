from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit')
def submitted():
    stocknamebuy = request.args.get('stocknamebuy')
    amountbuy = request.args.get('amountbuy')
    return render_template('result.html', stocknamebuy=stocknamebuy, amountbuy=amountbuy, message='Your form has been submitted successfully!')

@app.route('/process_form', methods=['POST'])
def process_form():
    
    stocknamebuy = request.form['stocknamebuy']
    amountbuy = request.form['amountbuy']

    # Redirect the user to the submitted page, passing the variables as arguments
    return redirect(url_for('submitted', stocknamebuy=stocknamebuy, amountbuy=amountbuy))
    
if __name__ == '__main__':
    app.run(debug=True)