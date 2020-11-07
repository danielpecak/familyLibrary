# familyLibrary
Simple database manager to organize a small (family size) set of books, including the history of borrowing.


---

## Name: 
**Biblioteka Rodziny Pęcaków** (Polish)

**Pęcak Family Library** (English)



## Symbol
Ex Libris Symbol
### Form
- full sticker
- stamp & sticker
- full sticker for the first page, a small stamp for the inside of the book

### Outlook/thema
- Daniel: physics symbol
 - Schroedinger cat
 - Dirac notation: <bra|ket>
 - atom symbol
 - Psi as a wavefunction
- Karo: 
 - bridge
 - metal construction
 - construction helmet
 - blueprint 
 - crane
 - tools
- animals?
  - owl
  - dog
- something that represents Marta and Romek
 - teddy bear
 - smile
 - rattle
 - ponytail
- general values
 - knowledge
 - books
 - environment
 - sensitivity

---

# Timetable
Here the timetable is shown. Within a workflow, the things should be done in order. The workflows are not dependent on each other (at least in the beginning).

Workflow #1
1. database structure in SQL
2. managing SQLite with python script 
3. fill in the database (partially)
4. ...
5. GUI
6. ...
7. fill in the database (completely)

Workflow #2
1. Talk about the design with Karo
2. Download vector graphics 
3. Make new graphics that are needed or when the licensing is not good for me
4. First draft of ex-libris
5. Second draft of ex-libris 

Workflow #3
1. QR generator function in python

Workflow #4
1. Website look

 ---

# **TODO** LIST
- [ ] ex libris draft
- [ ] QR generator (generate whenever a new item is added to **books** table)
- [ ] Database
 - [ ] code the structure
 - [ ] code test cases (use some real books on the shelf)
 - [ ] managing entries:
   - [ ] adding
   - [ ] removing
   - [ ] updating
 - [ ] dumping database for Git purposes (anonimizing the outuput)
- [ ] GUI
 - [ ] code basic view
   - [ ] listing: books, authors, borrowers
   - [ ] sorting books by Title, Language
 - [ ] managing entries
   - [ ] adding new entries to books, authors, borrowers 
   - [ ] removing entries from books, authors, borrowers
   - [ ] updating info about books, authors, borrowers
 - [ ] managing borrowings
   - [ ] borrower borrows book
   - [ ] book is returned
  
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
- ? publisher?
- ? lubimyczytac.pl link?
- ? owner?

*author*
- id
- first name
- last name


*borrower*
- id
- first name
- last name
- email
- phone number


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



### Table: Subcategories? Science/Children/etc?


