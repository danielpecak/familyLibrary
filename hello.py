#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from familyLibrary import app
from flask import Flask, render_template
import db, gui
app = Flask(__name__)
app.run(debug = True)

@app.route('/')
def hello_world():
    """Testing flask: part I."""
    return 'Hello, World!'

# @app.route('/daniel')
# def daniel():
#     """Testing flask: part II."""
#     return 'I co tam?!'

# @app.route('/hello/<user>')
# def hello_name(user):
#     """Testing flask: part III."""
#     return render_template('hello.html', name=user)
#     # return 'siema %s' % user
#     # user='asd'
#     # return render_template('hello.html', name=user)

@app.route('/book/<bookID>')
def book(bookID):
    """Shows the book website linked with QR on ex libris."""
    # Checks if the book exists in the library database
    error, msg = gui.check_book(bookID)
    if error:
        return render_template('bookError.html', message=msg)
    row = gui.show_book(bookID)
    print(row)
    if row[6]==None: #row[6]=end_date
        title  = row[0]
        author = row[1]+" "+row[2]
        status = "wypożyczone od "+str(row[5])+", od "+str(round(row[7]))+"dni, wypożyczający: "+row[3]+" "+row[4][0]+'.'

        # TODO calculate interwal: days, weeks, years
        return render_template('book.html', title=title, author=author,
                               status=status)
    else:
        title  = row[0]
        author = row[1]+" "+row[2]
        status = "W biblioteczce: można wypożyczać."
        return render_template('book.html', title=title, author=author,
                               status=status)

@app.route('/books')
def show_books():
    noofbooks, status, stats = gui.show_books()
    return render_template('books.html', noofbooks=noofbooks,status=status, stats=stats)

@app.route('/borrowed')
def show_borrowed():
    status, stats = gui.show_borrowed()
    return render_template('borrowed.html',status=status, stats=stats)

if __name__ == '__main__':
   app.run(debug = True)
