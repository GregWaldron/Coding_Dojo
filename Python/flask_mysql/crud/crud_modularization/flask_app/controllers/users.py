from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/process', methods=['POST'])
def process():
    User.save(request.form)
    return redirect('/users')

@app.route('/showuser/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("showUser.html",user=User.showOneUser(data))

@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.showOneUser(data))

@app.route('/destroy/<int:id>')
def destroy(id):
    User.destroy(id)
    return redirect ('/users')

@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    data ={ 
        "id":id
    }
    return redirect('/showuser/'+ request.form['id'])