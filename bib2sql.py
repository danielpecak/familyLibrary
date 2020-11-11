#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Scripts to transform BibTeX format to SQLite database

# import sqlite3 # NOTE not needed anymore at the moment

BIBTEXFILE="library.bib"

from pybtex.database.input import bibtex
from  db import *
conn = connection()
cur  = conn.cursor() 

parser = bibtex.Parser()
bibdata = parser.parse_file(BIBTEXFILE)

records=[]
for id in bibdata.entries:
    b = bibdata.entries[id].fields
    # for a in bibdata.entries[id].persons[unicode('author')]:
        # print id, unicode(a.first()[0]), unicode(a.last()[0])
    a = bibdata.entries[id].persons[unicode('author')][0]
    add_book(b["isbn"],b["title"],
    a.first()[0],a.last()[0],'Daniel',u'Pęcak',
    publisher=b["publisher"])
    records.append((None,unicode(a.first()[0]), unicode(a.last()[0])))
    # print b["year"]

# 
# cur.executemany('INSERT OR IGNORE INTO author VALUES(?,?,?);', records)
# print('# We have inserted '+str(cur.rowcount)+' records to the AUTHOR table.')
# 
# books=[]
# for id in bibdata.entries:
#     b = bibdata.entries[id].fields
#     books.append((b["isbn"],b["title"],b["publisher"]))
#     # print b["year"]
#     # print b["publisher"]
#     # print b["title"]
#     # print b["isbn"]
# 
# 
# cur.executemany('INSERT OR IGNORE INTO book(isbn,title,publisher) VALUES(?,?,?);', books)
# print('# We have inserted '+str(cur.rowcount)+' records to the BOOK table.')
# # TODO add owner
# # TODO add author


conn.commit()
conn.close()
add_tag('testowy')
add_author('Andrzej','Pilipiuk')
add_author('Andrzej','Pilipiuk')
add_author('Andrzej','Sapkowski')
add_person('Janina',u'Śmiałek')
add_person('Janina',u'Śmiałek')
add_person('Marta',u'Pęcak')
add_person('Dawid',u'Pęcak',email='dawid.pecak@gmail.com')

add_book('978-83-246-2716-5',
u'Lekarze, naukowcy, szarlatani. Od przerażonego pacjenta do świadomego konsumenta',
'Ben','Goldacre','Romek',u'Pęcak',
url='https://lubimyczytac.pl/ksiazka/88203/lekarze-naukowcy-szarlatani-od-przerazonego-pacjenta-do-swiadomego-konsumenta',
publisher='Septem',language='czeski',bookcase='Autralia',shelf='Sydney')


add_tag2book(8,3)

borrow(3,3)
borrow(7,3,'2018-10-10')
borrow(1,1)
borrow(2,1)
returnbook(3)
returnbook(2,'2021-01-21')
# returnbook(7,'2011-01-21')

# TODO add entries to database:
# add books