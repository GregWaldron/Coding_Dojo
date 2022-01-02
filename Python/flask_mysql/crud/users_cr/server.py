from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key = 'Consumer Reports'

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/process', methods=['POST'])
def process():
    users = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(users)
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)