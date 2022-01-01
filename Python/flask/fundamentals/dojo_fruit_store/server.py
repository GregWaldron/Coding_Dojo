from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__) 
app.secret_key = 'Hail Eris. All Hail Discordia.'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['qty'] = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    session['submit_time'] = datetime.now()
    print(f"Charging {session['first_name']} {session['last_name']} for {session['qty']} fruits")
    return redirect('/checkout')

@app.route('/checkout')         
def checkout():
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    