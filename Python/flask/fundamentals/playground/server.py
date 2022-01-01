from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("play_number_color.html", box_number=3, color="aqua")

@app.route('/play')
def play():
    return render_template("play_number_color.html", box_number=3, color="aqua")

@app.route('/play/<int:box_number>')
def play_number(box_number):
    return render_template("play_number_color.html", box_number=box_number, color="aqua")

@app.route('/play/<int:box_number>/<string:color>')
def play_number_color(box_number=3, color="aqua"):
    return render_template("play_number_color.html", box_number=box_number, color=color)

if __name__=="__main__":
    app.run(debug=True)