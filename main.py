# Assignment 3 Create a Flask application
# that allows users to add their reviews about English literature books data, stored in a.csv file.
# 3 routes home(/),/new,/book_review/<int:index>

from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)


# (/) GET home Show the home page to display Reviews of
# famous English Literature books.
# Route to display Reviews of famous English Literature books.
@app.route('/')
def index():
  with open('books.csv', 'r') as file:
    reader = csv.DictReader(file)
    reviews = list(reader)
  return render_template('index.html', reviews=reviews)


# /book/<int:index> GET	show_book show details of a specific item.
# Route to display individual book review details.
@app.route('/book/<int:index>')
def show_book(index):
  with open('books.csv', 'r') as file:
    reader = csv.DictReader(file)
    reviews = list(reader)
    review = reviews[index]
  return render_template('show.html', review=review)


# (/) POST	create add a new item to a collection.
# /new GET new Show the form to create a new item.
# Route to Add your review for a new book.
@app.route('/new', methods=['GET', 'POST'])
def create():
  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    rating = request.form['rating']
    review = request.form['review']

    with open('books.csv', 'a') as file:
      writer = csv.writer(file)
      writer.writerow([title, author, genre, rating, review])
    return redirect(url_for('index'))
  return render_template('new.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
