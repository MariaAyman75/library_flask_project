from flask_sqlalchemy import  SQLAlchemy
from flask import  url_for

db= SQLAlchemy()
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cover_photo = db.Column(db.String(250), nullable=True)
    pages_number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for('static', filename=f"books/images/{self.cover_photo}")

    @property
    def show_url(self):
        return url_for('books.details', book_id=self.id)

    @property
    def delete_url(self):
        return url_for('books.delete', book_id=self.id)
    
    @property
    def edit_url(self):
        return url_for('books.edit', book_id=self.id)

