from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit')
def submitted():
    return render_template('result.html', message='Your form has been submitted successfully!')

@app.route('/process_form', methods=['POST'])
def process_form():
    # Process the form data here
    # ...

    # Redirect the user to the submitted page
    return redirect(url_for('submitted'))

if __name__ == '__main__':
    app.run(debug=True)