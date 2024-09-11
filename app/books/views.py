from app.models import Book, db
from flask import render_template, request, redirect, url_for
from app.books import  book_blueprint
from app.books.forms import BookForm
import os
from werkzeug.utils import secure_filename

@book_blueprint.route("", endpoint="home") 
def home():
    books = Book.query.all()
    return render_template("books/home.html", books=books)

@book_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def create():
    form = BookForm()
    if request.method == "POST" and form.validate_on_submit():
        image_name=None
        if request.files.get('cover_photo'):
             cover_photo= form.cover_photo.data
             image_name =secure_filename(cover_photo.filename)
             cover_photo.save(os.path.join('app/static/books/images/', image_name))
        book = Book(title=request.form["title"],cover_photo=image_name,
                     pages_number= request.form["pages_number"] ,description=request.form["description"] )
        db.session.add(book)
        db.session.commit()
        return redirect(book.show_url)
    return render_template("books/create.html", form=form)

@book_blueprint.route("<int:book_id>", endpoint="details")
def details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("books/details.html", book=book)

@book_blueprint.route("/<int:book_id>/edit", endpoint="edit", methods=["GET", "POST"])
def edit(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm(obj=book)
    if request.method == "POST" and form.validate_on_submit():
        book.title = form.title.data
        book.pages_number = form.pages_number.data
        book.description = form.description.data
        if request.files.get('cover_photo'):
            cover_photo= form.cover_photo.data
            image_name =secure_filename(cover_photo.filename)
            cover_photo.save(os.path.join('app/static/books/images/', image_name))
            book.cover_photo = image_name
        db.session.commit()
        return redirect(book.show_url)
    return render_template("books/edit.html", form=form, book=book)

@book_blueprint.route("<int:book_id>/delete", endpoint="delete", methods=['POST'])
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.home'))

