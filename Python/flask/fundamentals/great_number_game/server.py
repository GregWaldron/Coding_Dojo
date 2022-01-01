from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'woirejokjen302398ijh'

@app.route('/')
def index():
    if "message" not in session:
        session['target'] = random.randint(1,100)
        session['guess_count'] = 0
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['guess_count'] += 1
    if int(request.form['user_guess']) < session['target']:
        session['message'] = "Too low."
        session['color'] = "red"
    elif int(request.form['user_guess']) > session['target']:
        session['message'] = "Too high."
        session['color'] = "red"
    else:
        session['message'] = "BINGO!"
        session['color'] = "green"
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


