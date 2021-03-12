
from flask import Flask, render_template, request, redirect, session, render_template_string
godNum = Flask(__name__)
# (no sensitive data to worry about)
godNum.secret_key = 'secretkey'

# home page
@godNum.route('/')
def index():
    return render_template('index.html')

# dividends calculator input
@godNum.route('/dividends')
def dividendsInput():
    if not session['dividendsDividendLimit']:
        session['dividendsDividendLimit'] = 0
    if not session['dividendsDivisorLimit']:
        session['dividendsDivisorLimit'] = 0
    return render_template('dividends.html', dividendLimit = session['dividendsDividendLimit'], divisorLimit = session['dividendsDivisorLimit'])

@godNum.route('/dividends/calculate', methods=['POST'])
def dividendsCalculate():
    session['dividendsDividendLimit'] = request.form['dividendLimit']
    session['dividendsDivisorLimit'] = request.form['divisorLimit']
    return redirect('/dividends/results')

@godNum.route('/dividends/results')
def dividendsResults():
    return render_template('dividends_results.html', dividendLimit = session['dividendsDividendLimit'], divisorLimit = session['dividendsDivisorLimit'])

# factor calculator input
@godNum.route('/factors')
def factorsInput():
    if not session['factorsDivisorLimit']:
        session['factorsDivisorLimit'] = 0
    if not session['factorsDividendLimit']:
        session['factorsDividendLimit'] = 0
    return render_template('factors.html', divisorLimit = session['factorsDivisorLimit'], dividendLimit = session['factorsDividendLimit'])

@godNum.route('/factors/calculate', methods=['POST'])
def factorsCalculate():
    session['factorsDivisorLimit'] = request.form['divisorLimit']
    session['factorsDividendLimit'] = request.form['dividendLimit']
    return redirect('/factors/results')

@godNum.route('/factors/results')
def factorsResults():
    return render_template('factors_results.html', divisorLimit = session['factorsDivisorLimit'], dividendLimit = session['factorsDividendLimit'])

# Ensure this file is being run directly and not from a different module    
if __name__=="__main__":   
    godNum.run(debug=False)