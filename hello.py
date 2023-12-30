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



def renderAndsave(func):
    """Rendering website and saving html code."""
    def inner(*args, **kwargs):
        html = func(*args, **kwargs)
        filename = "book{:04d}.html".format(int(kwargs['bookID']))
        # print(filename)
        text_file = open(filename, "w")
        text_file.write(html)
        text_file.close()
        return(html)
    return inner


@app.route('/book/<bookID>')
# @renderAndsave
def bookbook(bookID):
    return gui.book(bookID)




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
