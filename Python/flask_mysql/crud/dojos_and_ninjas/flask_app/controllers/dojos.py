from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojos.html",dojos=Dojo.get_all())

@app.route('/processDojos', methods=['POST'])
def processDojos():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojoShow(id):
    data ={ 
        "id":id
    }
    return render_template("dojoShow.html",dojo=Dojo.showNinjas(data))