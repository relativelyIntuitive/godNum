
from flask import Flask, render_template, request, redirect, session, render_template_string
godNum = Flask(__name__)
# (no sensitive data to worry about)
godNum.secret_key = 'secretkey'

def render_js(fname, *args):
    with open(fname) as fin:
        script = fin.read()
        rendered_script = render_template_string(script, *args)
        return rendered_script

# home page
@godNum.route('/')
def index():
    return render_template('index.html')

# dividends calculator input
@godNum.route('/dividends')
def dividendsInput():
    return render_template('dividends.html')

@godNum.route('/dividends/calculate', methods=['POST'])
def dividendsCalculate():
    session['dividendsDividendLimit'] = request.form['dividendLimit']
    session['dividendsDivisorLimit'] = request.form['divisorLimit']
    # jsDividends = render_js('godNumDividends.js', p1 = session['dividendsDividendLimit'], p2 = session['dividendsDivisorLimit'])
    # session['dividendsResults'] = jsDividends
    return redirect('/dividends/results')

@godNum.route('/dividends/results')
def dividendsResults():
    return render_template('dividends_results.html', dividendLimit = session['dividendsDividendLimit'], divisorLimit = session['dividendsDivisorLimit'])

# factor calculator input
@godNum.route('/factors')
def factorsInput():
    return render_template('factors.html')

@godNum.route('/factors/calculate', methods=['POST'])
def factorsCalculate():
    session['factorsDivisorLimit'] = request.form['divisorLimit']
    session['factorsDividendLimit'] = request.form['dividendLimit']
    # jsFactors= render_js('godNumFactors.js', p1 = session['factorsDivisorLimit'], p2 = session['factorsDividendLimit'])
    # session['factorsResults'] = jsFactors
    return redirect('/factors/results')

@godNum.route('/factors/results')
def factorsResults():
    return render_template('factors_results.html', divisorLimit = session['factorsDivisorLimit'], dividendLimit = session['factorsDividendLimit'])

# Ensure this file is being run directly and not from a different module    
if __name__=="__main__":   
    godNum.run(debug=True)