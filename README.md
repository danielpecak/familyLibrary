# familyLibrary
# familyLibrary

log items that has been ignored including the history of borrowing.

---

## How to run:
### Dependencies (and versions):
 * flask
 * werkzeug
 * pybtex

``sudo apt-get install python3-pybtex``

``sudo apt-get install python3-flask``

``sudo apt-get install python3-qrcode``

Run in the command line (or ``--debug run``):
``flask --app hello.py run``

### Testing database
Making 'example.db' based on 'DBstructure.sql'.
To setup the database:
  * `rm example.db`
  * `./init_db.py`
  * `./bib2sql.py`

###

---

## Name:
**Biblioteka Rodziny Pęcaków** (Polish)

**Pęcak Family Library** (English)



## Symbol
Ex Libris Symbol: decided to be a steampunk owl with QR code and caption "Ex libris of Pęcak family". The size will be 6x6cm with 2x2cm QR code. It will be printed on a sticker and stick to the back cover (Karo) or at the beginning (probably blank page) of the book.

### Form
- full sticker
- ~~stamp & sticker~~
- ~~full sticker for the first page, a small stamp for the inside of the book~~


---

# Timetable
Here the timetable is shown. Within a workflow, the things should be done in order. The workflows are not dependent on each other (at least in the beginning).

Workflow #1
1. ~~database structure in SQL~~
2. ~~managing SQLite with python script ~~
3. ~~fill in the database (partially)~~
4. ...
5. GUI
6. ...
7. fill in the database (completely)

Workflow #2
1. ~~Talk about the design with Karo~~
2. ~~Download vector graphics: make tests~~
3. ~~Talk with a designer~~
4. First draft of ex-libris
5. Tests for printing and QR code
6. Second draft/final version of ex-libris

Workflow #3
1. QR generator function in python
2. function for embedding QR code into graphics
3. generating an A4 page of sticker ready to print

Workflow #4
1. Website look
2. Look for nice CSS styles
3. generate an up-to-date websites for QR codes

---

# **TODO** LIST
- [ ] ex libris
 - [X] brain storming
 - [ ] ~~pencil drafts~~
 - [X] brain storming: choosing best
 - [X] asking third party for graphics
 - [X] size testing
 - [ ] final choice
- [X] BiBTeX to SQL converter
 - [X] library for conversion (pybtex)
 - [X] authors
 - [X] books: first step
 - [X] books: foreign indices
- [ ] QR generator (generate whenever a new item is added to **books** table)
 - [X] draft of generator
 - [X] use *qrcode* library in more sophisticated way
 - [X] function **generateQR(url_text,path/filename)**
 - [X] testing QR code sizes
 - [ ] generating pdf file for printing QR codes
 - [ ] function **update_qrs(dir,?)** that reads all the qrs from *dir* and changes them to the desired new format (update links or change the size of qrs). Maybe update should be done based on database content
- [ ] Database
 - [X] code the structure
 - [X] add table with tag names to the structure
 - [X] add relation table for tags and books
 - [ ] managing entries (write functions):
   - [X] adding
   - [ ] removing
   - [ ] updating
 - [ ] code test cases (use some real books on the shelf)
   - [X] code people (owners and borrowers)
   - [ ] code books
   - [ ] real testing: code actions
     - [X] adding books to library
     - [X] adding new people
     - [X] adding borrowing books
     - [ ] updating books
     - [ ] updating borrowers
     - [ ] updating authors
     - [ ] adding authors to book
     - [ ] destroying books (lost flag=1, removing relations)
 - [ ] dumping database for Git purposes (anonimizing the outuput)
  - [X] managing borrowings
    - [X] borrower borrows book
    - [X] book is returned
- [ ] GUI
 - [X] static html code basic view
 - [ ] implement flask
 - [ ] incorporate static listing
 - [ ] implement dynamic sorting on columns
   - [X] listing: books, authors, borrowers
   - [ ] ~~sorting books by Title, Language~~
 - [ ] managing entries
   - [ ] adding new entries to books, authors, borrowers
   - [ ] removing entries from books, authors, borrowers
   - [ ] updating info about books, authors, borrowers

---

# **TODO2** LIST: things for later
- [ ] adding books: author and owner should be a list type
- [X] log items that has been ignored
- [ ] add archive_tables and store there destroyed books, and returned books
   - [ ] use TRIGGERS to do that

---

## QR generator
- generates a QR code with a link of type
  https://danielpecak.github.io/lib?id=123/ that gives some info
- print QR sticker and stick it


## Website
what should be given under the link where QR code directs
- some basic info about the book
- when the book has been borrowed
- initials of the borrower
- if the book is not borrowed write that it is free
- option of reservation for someone? this can be done by borrowing it in the system, but not physically

## Languages
- core: python
- GUI: HTML-based GUI?
- database: SQLite
- website: javascript? git supports static websites



## Database structure

### Tables
*book*
- id
- ISBN
- title
- author (what with many authors or encyclopedias)
- language
- destroyed/given_away/lost
- publisher
- lubimyczytac.pl link
- owner
- bookcase (name bookcases after continents Europe, America, etc.)
- shelf (name after cities or countries: Amsterdam, Wiedeń, etc.)

*author*
- id
- first name
- last name

*tag*
- id
- name


*borrower*
- id
- first name
- last name
- email
- phone number

*owner*
- id
- first name
- last name
- email
- phone number

? scalić *borrower* i *owner*?

### Relations
*borrowing* (book-borrower)
- id
- id_book
- id_who
- start_date
- end_date

*written* (book-author)
- id
- id_book
- id_author

*hastag* (book-tag)
- id
- id_book
- id_tag




### Table: Subcategories? Science/Children/etc?
