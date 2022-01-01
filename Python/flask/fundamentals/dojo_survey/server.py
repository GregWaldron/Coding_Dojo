from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Justice League'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    if "Running" in request.form:
        session['running'] = request.form['Running']
    if "Crime-Fighting" in request.form:
        session['crime-fighting'] = request.form['Crime-Fighting']
    if "Flying" in request.form:
        session['flying'] = request.form['Flying']
    if "Gadgets" in request.form:
        session['gadgets'] = request.form['Gadgets']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)