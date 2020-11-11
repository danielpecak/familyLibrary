#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import os 
import sys

DB_NAME='example.db'
INIT_SQL='DBstructure.sql'


def connection():
    """Connects to the database."""
    conn = sqlite3.connect(DB_NAME)
    # cur=conn.cursor()
    conn.execute('PRAGMA foreign_keys = ON;')
    conn.commit()
    try:
        # print("# Connected to database: %s"%(DB_NAME))
        return conn
    except sqlite3.Error as e:
        pass
        # print("I am unable to connect to the database: %s" % e.args[0])

def add_author(fname,lname):
    """Description """
    c=connection()
    cur=c.cursor()
    cur.execute('INSERT OR IGNORE INTO author(first_name,last_name) VALUES(?,?);',(fname,lname))
    if(cur.rowcount==1):
        print("# Author '%s %s' added to database %s"%(fname,lname,DB_NAME))
    else:
        print("# Author '%s %s' already exists in the database %s"%(fname,lname,DB_NAME))
    c.commit()    
    c.close()
    return cur.lastrowid

def add_tag(tag):
    """Description """
    c=connection()
    cur=c.cursor()
    cur.execute('INSERT OR IGNORE INTO tag(name) VALUES(?);',(tag,))
    if(cur.rowcount==1):
        print("# Tag '%s' added to database %s"%(tag,DB_NAME))
    else:
        print("# Tag '%s' already exists in the database %s"%(tag,DB_NAME))
    c.commit()    
    c.close()
    return cur.lastrowid

def add_person(fname,lname,email=None,phone=None):
    """Description """
    c=connection()
    cur=c.cursor()
    cur.execute('INSERT OR IGNORE INTO people(first_name,last_name,email,phone) VALUES(?,?,?,?);',(fname,lname,email,phone))
    if(cur.rowcount==1):
        print("# Person '%s %s (Email:%s, Phone:%s)' added to database %s"%(fname,lname,email,phone,DB_NAME))
    else:
        print("# Person '%s %s (Email:%s, Phone:%s)' already exists in the database %s"%(fname,lname,email,phone,DB_NAME))
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
        
    cur.execute('INSERT OR IGNORE INTO book(isbn,title,url,language,publisher,bookcase,shelf) VALUES(?,?,?,?,?,?,?);',(isbn,title,url,language,publisher,bookcase,shelf))
    bookID=cur.lastrowid
    
    if(bookID!=0):
        # TODO add INSERT OR IGNORE
        cur.execute('INSERT INTO book_R_author(id_book,id_author) VALUES(?,?);', (bookID,authorID))

        # TODO add INSERT OR IGNORE
        cur.execute('INSERT INTO ownership(id_book,id_people) VALUES(?,?);', (bookID,ownerID))
    
    if(cur.rowcount==1):
        print("# Book '%s' added to database %s"%(title,DB_NAME))
    else:
        print("# Book '%s' already exists in the  database %s"%(title,DB_NAME))
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
        cur.execute('INSERT OR IGNORE INTO book_R_tag(id_book,id_tag) VALUES(?,?);',(bookID,tagID))
    if(cur.rowcount==1):
        print("# Tag '%s' added to the book '%s'"%(tagNAME,bookTITLE))
    else:
        print("# Tag '%s' already is connected to the book  '%s'"%(tagNAME,bookTITLE))
    c.commit()    
    c.close()
    return cur.lastrowid

def borrow(bookID,personID,start=None):
    """Description """
    c=connection()
    cur=c.cursor()
    if(start):
        cur.execute('INSERT OR IGNORE INTO borrowings(id_book,id_people,start_date) VALUES(?,?,?);',(bookID,personID,start))
    else:
        cur.execute('INSERT OR IGNORE INTO borrowings(id_book,id_people) VALUES(?,?);',(bookID,personID))
    print("# The book has been borrowed")
    c.commit()    
    c.close()

def returnbook(bookID,end=None):
    """Description """
    c=connection()
    cur=c.cursor()
    if(end):
        cur.execute('UPDATE borrowings SET end_date=? WHERE id_book=? AND end_date IS NULL;',(end,bookID))
    else:
        cur.execute('UPDATE borrowings SET end_date=date("now") WHERE id_book=? AND end_date IS NULL;',(bookID,))
    c.commit()    
    print("# The book has been returned.")
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
