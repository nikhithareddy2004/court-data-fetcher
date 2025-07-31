from flask import Flask, render_template, request
from scraper import fetch_case_data

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        year = request.form['year']
        try:
            result = fetch_case_data(case_type, case_number, year)
        except Exception as e:
            error = str(e)
    return render_template('index.html', result=result, error=error)

if _name_ == '_main_':
    app.run(debug=True)
