#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generating simple GUI
from  db import *

HEADER = """<html>
<head>
<link rel="stylesheet" href="css.css"></head>
<body>
<a href="html_books.html">Books</a>      </br>
<a href="html_borrowed.html">Borrowed</a></br>
</br>
"""
FOOTER = """
</body></html>
"""

def show_books():
    f = open('html_books.html','wb+')
    f.write(HEADER)
    conn = connection()
    cur  = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM book WHERE annihilated=0;")
    noofbooks = cur.fetchone()[0]
    
    f.write("<h3>Stan biblioteki: %s pozycji</h3>"%(noofbooks,))
    cur.execute("""
    SELECT book.title, author.first_name, author.last_name, book.bookcase, book.shelf, max(borrowings.end_date IS NULL AND borrowings.start_date IS NOT NULL) as isborrowed
    FROM book 
    INNER JOIN book_R_author ON book_R_author.id_book=book.id 
    INNER JOIN author        ON book_R_author.id_author=author.id 
    LEFT JOIN borrowings     ON borrowings.id_book=book.id 
    WHERE book.annihilated=0
    GROUP BY book.id;
    """)
    f.write("<table>\n")
    f.write("""<tr>    <td>Tytuł</td>    <td>Autor</td>    <td>Dostępność</td>    </tr>\n""")
    rows=cur.fetchall()
    status=[]
    for r in rows:
        f.write("<tr>")
        title=r[0].encode('utf-8')
        author=r[1].encode('utf-8')+" "+r[2].encode('utf-8')
        freeFlag=r[5]
        # print(freeFlag)
        if r[3] is None:
            loc="Europa"
        else:
            loc=str(r[3]).encode('utf-8')+"."+str(r[4]).encode('utf-8')
        if(freeFlag):
            loc2="<p class='stress'>Niedostępne</p>"
        else:
            loc2=loc
        m=("<td class='booktitle'>%s</td><td>%s</td><td>%s</td>"%(title,author,loc2))
        if(freeFlag):
            loc2="Niedostępne"
        else:
            loc2=loc
        status.append((r[0],r[1]+" "+r[2],freeFlag, loc2.decode('utf-8')))
        # status.append((title,author,freeFlag,loc2))
        f.write(m)
        f.write("</tr>\n")
    f.write("</table></br>")

    cur.execute("""
    SELECT author.first_name, author.last_name, COUNT(author.id) as nr 
    FROM book 
    INNER JOIN book_R_author ON book_R_author.id_book=book.id 
    INNER JOIN author ON book_R_author.id_author=author.id 
    WHERE book.annihilated=0
    GROUP BY author.id 
    HAVING nr>1 
    ORDER BY nr DESC;
    """)
    f.write("<table>\n")
    f.write("<h3>Statystyka autorów</h3>\n")
    f.write("""<tr>  <td>Autor</td>    <td>Ile książek</td>    </tr>\n""")
    rows=cur.fetchall()
    stats=[]
    for r in rows:
        f.write("<tr>")
        author=r[0].encode('utf-8')+" "+r[1].encode('utf-8')
        howmany=r[2]
        m=("<td>%s</td><td>%s</td>"%(author,howmany))
        stats.append((r[0]+" "+r[1],r[2]))
        # stats.append((author,howmany))
        f.write(m)
        f.write("</tr>\n")
    f.write("</table>")
    f.write(FOOTER)
    conn.close()
    f.close()
    return noofbooks, status, stats

def calcTime(ddays):
    # TODO form
    days=int(ddays)
    # print(ddays)
    # print(days)
    if(days==0):
        return "dzisiaj"
    if(days==1):
        return "1 dzień temu"
    elif(days>365*2):
        return "%s l temu"%(days/365,)
        form="lat" if days>=5*365 else "lata"
        return "%s %s temu"%(days/365,form)
    elif((days>7*8) and (days<=31*24)):
        return "%s m temu"%(days/30,)
        form="miesięcy" if days>=5*30 else "miesiące"
        return "%s %s temu"%(days/30,form)
    elif((days>14) and (days<=7*8)):
        return "%s tyg. temu"%(days/7,)
        form="tygodni" if days>=5*7 else "tygodnie"
        return "%s %s temu"%(days/7,form)
    else:
        return "%s d temu"%(days,)
        return "%s dni temu"%(days,)

    

def show_borrowed():
    f = open('html_borrowed.html','wb+')
    f.write(HEADER)
    conn = connection()
    cur  = conn.cursor()
    cur.execute("""
    SELECT book.title, author.first_name, author.last_name, people.first_name, people.last_name, borrowings.start_date, julianday('now') - julianday(borrowings.start_date  )
    FROM borrowings
    INNER JOIN book ON borrowings.id_book=book.id 
    INNER JOIN people ON borrowings.id_people=people.id 
    INNER JOIN book_R_author ON book_R_author.id_book=book.id 
    INNER JOIN author ON book_R_author.id_author=author.id 
    WHERE book.annihilated=0 AND  borrowings.end_date IS NULL
    ORDER BY people.last_name;
    """)
    f.write("<table>\n")
    f.write("""<tr>    <td>Tytuł</td>    <td>Autor</td>    <td>Wypożyczający</td> <td>Kiedy wypożyczone</td>    </tr>\n""")
    rows=cur.fetchall()
    status = []
    for r in rows:
        # print(r)
        f.write("<tr>")
        title=r[0].encode('utf-8')
        author=r[1].encode('utf-8')+" "+r[2].encode('utf-8')
        borrower=r[3].encode('utf-8')+" "+r[4].encode('utf-8')
        # print(title,author,borrower)
        m=("<td class='booktitle'>%s</td><td>%s</td><td>%s</td><td>%s</td>"%(title,author,borrower,calcTime(r[6])))
        f.write(m)
        status.append((r[0],r[1]+" "+r[2],r[3]+" "+r[4],calcTime(r[6])))
        f.write("</tr>\n")
    f.write("</table></br>")
    
    cur.execute("""
    SELECT people.first_name, people.last_name, COUNT()
    FROM borrowings
    INNER JOIN book ON borrowings.id_book=book.id 
    INNER JOIN people ON borrowings.id_people=people.id 
    INNER JOIN book_R_author ON book_R_author.id_book=book.id 
    INNER JOIN author ON book_R_author.id_author=author.id 
    WHERE book.annihilated=0 AND  borrowings.end_date IS NULL
    GROUP BY people.last_name
    ORDER BY people.last_name;
    """)
    f.write("<table>\n <h3>Statystyki wypożyczeń</h3>")
    f.write("""<tr>  <td>Wypożyczający</td> <td>Liczba książek</td>    </tr>\n""")
    rows=cur.fetchall()
    stats=[]
    for r in rows:
        # print(r)
        f.write("<tr>")
        borrower=r[0].encode('utf-8')+" "+r[1].encode('utf-8')
        howmany=r[2]
        m=("<td>%s</td><td>%s</td>"%(borrower,howmany))
        stats.append((r[0]+" "+r[1],howmany))
        f.write(m)
        f.write("</tr>\n")
    f.write("</table>")
    
    
    f.write(FOOTER)
    conn.close()
    f.close()
    return status, stats

returnbook(3)

show_books()
show_borrowed()
    