from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def books():
    return render_template("books.html",all_books=Book.get_all())

@app.route('/newBook', methods=['POST'])
def newBook():
    data = {
        "title":request.form['title'],
        "num_of_pages":request.form['num_of_pages']
    }
    book_id = Book.save(request.form)
    return redirect('/books')

@app.route('/books/<int:id>')
def showBook(id):
    data ={ 
        "id":id
    }
    return render_template("showBook.html",book=Book.showAuthors(data),unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/addFavoriteAuthor', methods=['POST'])
def addFavoriteAuthor():
    data = {
        "author_id":request.form['author_id'],
        "book_id":request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")