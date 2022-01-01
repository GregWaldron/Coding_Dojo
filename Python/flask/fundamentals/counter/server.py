from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'woirejokjen302398ijh'

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 1
        session['fake_count'] = 1
    else:
        session['count'] +=1
        session['fake_count'] +=1
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    session['fake_count'] = session['count'] + int(request.form['number'])
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


