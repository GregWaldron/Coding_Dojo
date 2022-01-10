from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("authors.html",all_authors=Author.get_all())

@app.route('/newAuthor', methods=['POST'])
def newAuthor():
    data = {
        "name":request.form['name']
    }
    author_id = Author.save(request.form)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def showAuthor(id):
    data ={ 
        "id":id
    }
    return render_template("showAuthor.html",author=Author.showBooks(data), unfavorited_books=Book.unfavorited_books(data))

@app.route('/addFavoriteBook', methods=['POST'])
def addFavoriteBook():
    data = {
        "author_id":request.form['author_id'],
        "book_id":request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")