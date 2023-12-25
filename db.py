#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Utils for managing database in encapsulated form

import sqlite3
import os
import sys
import logger

DB_NAME='example.db'
INIT_SQL='DBstructure.sql'


def connection():
    """Connects to the database."""
    conn = sqlite3.connect(DB_NAME)
    # cur=conn.cursor()
    conn.execute('PRAGMA foreign_keys = ON;')
    conn.commit()
    try:
        logger.add("Connected to database: %s"%(DB_NAME),4)
        return conn
    except sqlite3.Error as e:
        pass
        logger.add("I am unable to connect to the database: %s" % e.args[0],1)

def add_author(fname,lname):
    """Description """
    c=connection()
    cur=c.cursor()
    try:
        cur.execute('INSERT  INTO author(first_name,last_name) VALUES(?,?);',(fname,lname))
    except sqlite3.Error as er:
        logger.add('SQLite error: %s' % (' '.join(er.args)),1)

    if(cur.rowcount==1):
        logger.add("Author '%s %s' added to database %s"%(fname,lname,DB_NAME),3)
    else:
        logger.add("Author '%s %s' already exists in the database %s"%(fname,lname,DB_NAME),3)
    c.commit()
    c.close()
    return cur.lastrowid

def add_tag(tag):
    """Description """
    c=connection()
    cur=c.cursor()
    try:
        cur.execute('INSERT  INTO tag(name) VALUES(?);',(tag,))
    except sqlite3.Error as er:
        logger.add('SQLite error: %s' % (' '.join(er.args)),1)

    if(cur.rowcount==1):
        logger.add("Tag '%s' added to database %s"%(tag,DB_NAME),3)
    else:
        logger.add("Tag '%s' already exists in the database %s"%(tag,DB_NAME),2)
    c.commit()
    c.close()
    return cur.lastrowid

def add_person(fname,lname,email=None,phone=None):
    """Description """
    c=connection()
    cur=c.cursor()
    try:
        cur.execute('INSERT  INTO people(first_name,last_name,email,phone) VALUES(?,?,?,?);',(fname,lname,email,phone))
    except sqlite3.Error as er:
        logger.add('SQLite error: %s' % (' '.join(er.args)),1)

    if(cur.rowcount==1):
        logger.add("Person '%s %s (Email:%s, Phone:%s)' added to database %s"%(fname,lname,email,phone,DB_NAME),3)
    else:
        logger.add("Person '%s %s (Email:%s, Phone:%s)' already exists in the database %s"%(fname,lname,email,phone,DB_NAME),2)
    c.commit()
    c.close()
    return cur.lastrowid

def add_book(isbn,title,fauthor,lauthor,fowner,lowner,url=None,publisher=None,language=None,bookcase=None,shelf=None):#structure to the argument?
    """Description """
    c=connection()
    cur=c.cursor()
    # Checks if Author exists, if not, creates one.
    cur.execute('SELECT rowid FROM "author" WHERE first_name=? AND last_name=?;', (fauthor,lauthor))
    l = cur.fetchall()
    if (len(l)==0):
        authorID = add_author(fauthor,lauthor)
    else:
        authorID = l[0][0]

    # Checks if Owner exists, if not, creates one.
    cur.execute('SELECT rowid FROM "people" WHERE first_name=? AND last_name=?;', (fowner,lowner))
    l = cur.fetchall()
    if (len(l)==0):
        ownerID = add_person(fowner,lowner)
    else:
        ownerID = l[0][0]

    try:
        cur.execute('INSERT  INTO book(isbn,title,url,language,publisher,bookcase,shelf) VALUES(?,?,?,?,?,?,?);',(isbn,title,url,language,publisher,bookcase,shelf))
    except sqlite3.Error as er:
        logger.add('SQLite error: %s' % (' '.join(er.args)),1)
    bookID=cur.lastrowid

    if((bookID!=0) and (bookID is not None)):
        # print(2)
        # TODO add INSERT OR IGNORE
        try:
            cur.execute('INSERT INTO book_R_author(id_book,id_author) VALUES(?,?);', (bookID,authorID))
        except sqlite3.Error as er:
            logger.add('SQLite error: %s' % (' '.join(er.args)),1)

        # TODO add INSERT OR IGNORE
        try:
            cur.execute('INSERT INTO ownership(id_book,id_people) VALUES(?,?);', (bookID,ownerID))
        except sqlite3.Error as er:
            logger.add('SQLite error: %s' % (' '.join(er.args)),1)

    if(cur.rowcount==1):
        logger.add("Book '%s' added to database %s"%(title,DB_NAME),3)
    else:
        logger.add("Book '%s' already exists in the  database %s"%(title,DB_NAME),2)
    c.commit()
    c.close()

def add_tag2book(tagID,bookID):
    """Description """
    c=connection()
    cur=c.cursor()
    cur.execute('SELECT COUNT(*),title FROM "book" WHERE id=?', (bookID,))
    temp=cur.fetchone()
    bookEXIST=temp[0]
    bookTITLE=temp[1]
    cur.execute('SELECT COUNT(*),name FROM "tag" WHERE id=?', (tagID,))
    temp=cur.fetchone()
    tagEXIST=temp[0]
    tagNAME=temp[1]
    if(tagEXIST*bookEXIST==1):
        try:
            cur.execute('INSERT  INTO book_R_tag(id_book,id_tag) VALUES(?,?);',(bookID,tagID))
        except sqlite3.Error as er:
            logger.add('SQLite error: %s' % (' '.join(er.args)),1)

    if(cur.rowcount==1):
        logger.add("Tag '%s' added to the book '%s'"%(tagNAME,bookTITLE),3)
    else:
        logger.add("Tag '%s' already is connected to the book  '%s'"%(tagNAME,bookTITLE),2)
    c.commit()
    c.close()
    return cur.lastrowid

def borrow(bookID,personID,start=None):
    """
Borrows a book with 'bookID' to a person with 'personID'.
When no start date is given, today date is set.
"""
    c=connection()
    cur=c.cursor()
    cur.execute('SELECT * FROM borrowings WHERE id_book=? AND start_date IS NOT NULL AND end_date IS NULL;',(bookID,))
    row=cur.fetchone()
    available=True if (row==None) else False
    if(available==False):
        logger.add("Book with id=%d is not available (someone is reading it)."%(bookID,),1)
        return
    # print(row,available)
    if(start):
        try:
            cur.execute('INSERT  INTO borrowings(id_book,id_people,start_date) VALUES(?,?,?);',(bookID,personID,start))
        except sqlite3.Error as er:
            logger.add('SQLite error: %s' % (' '.join(er.args)),1)
    else:
        try:
            cur.execute('INSERT  INTO borrowings(id_book,id_people) VALUES(?,?);',(bookID,personID))
        except sqlite3.Error as er:
            logger.add('SQLite error: %s' % (' '.join(er.args)),1)

    logger.add("The book with id=%d has been borrowed"%(bookID,),3)
    c.commit()
    c.close()

def returnbook(bookID,end=None):
    """
Returns book with bookID to the set of books that are not borrowed. If the date of
return is not given, it is set by default to today.
If the book is not borrowed, it gives an error in the log.
    """
    c=connection()
    cur=c.cursor()
    cur.execute('SELECT * FROM borrowings WHERE id_book=? AND start_date IS NOT NULL AND end_date IS NULL;',(bookID,))
    if(cur.fetchone() is None):
        logger.add("Book with id=%d is not borrowed, it's on the shelf."%(bookID,),1)
        return

    if(end):
        cur.execute('UPDATE borrowings SET end_date=? WHERE id_book=? AND end_date IS NULL;',(end,bookID))
    else:
        cur.execute('UPDATE borrowings SET end_date=date("now") WHERE id_book=? AND end_date IS NULL;',(bookID,))
    c.commit()
    logger.add("The book has been returned.",3)
    c.close()



def update_author(id,fname,lname):
    """Description """
    pass

def update_tag(id,tag):
    """Description """
    pass


def update_person(id,fname,lname,email=None,phone=None):
    """Description """
    pass

def update_book(id,isbn,title,fauthor,lauthor,fowner,lowner,url=None,language=None,bookcase=None,shelf=None):#structure to the argument?
    """Description """
    # add to book table
    # add new author if needed and it does not exist
    # add to book-author table
    # add new owner if needed and it does not exist
    # add to book-owner table
    # add new tag if needed and it does not exist
    # add to book-tag table
    pass

# TODO how to manage deletions? CASCADE? remove authors AND books?
# def del_author() # TODO how to manage it
# def del_book() # TODO how to manage it
