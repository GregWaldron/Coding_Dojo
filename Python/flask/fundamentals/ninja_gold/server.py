from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__) 
app.secret_key = 'Stay gold, Ponyboy.'

@app.route('/')         
def index():
    if "balance" not in session:
        session['balance'] = 0
    if "log" not in session:
        session['log'] = []
    if "building" not in session:
        session['buildings'] =  {
                                'farm': (10,20),
                                'cave': (5,10),
                                'house': (2,5),
                                'casino': (-50,50)
                                }
    if "turn_count" not in session:
        session['turn_count'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    session['turn_count'] += 1
    session['amount'] = random.randint(session['buildings'][request.form['building']][0],session['buildings'][request.form['building']][1])
    session['balance'] += session['amount']
    session['log'].append(["Turn " + str(session['turn_count']) + ": Earned " + str(session['amount']) + " from the " + request.form['building'] + "(" + str(datetime.now()) + ")", session['amount']])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)