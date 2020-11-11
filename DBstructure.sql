PRAGMA FOREIGN_KEYS=OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS ownership;
DROP TABLE IF EXISTS borrowings;
DROP TABLE IF EXISTS book_R_author;
DROP TABLE IF EXISTS book_R_tag;

--  TODO add autoincrement

CREATE TABLE book
(
  id    integer PRIMARY KEY NOT NULL,
  isbn  character varying NOT NULL,
  title character varying NOT NULL,
  url   character varying, --- link to lubimyczytac.pl
  annihilated boolean DEFAULT 0, --- 0 when in library, 1 when lost/destroyed/given away
  language    character varying DEFAULT 'polski', --- Polish/English
  publisher   character varying,
  bookcase    character varying,
  shelf       character varying,
  UNIQUE(isbn)
);
-- author 
-- owner


CREATE TABLE author
(
  id  integer PRIMARY KEY,
  first_name character varying NOT NULL,
  last_name  character varying NOT NULL,
  
  UNIQUE(first_name,last_name)
);

CREATE TABLE tag
(
  id  integer PRIMARY KEY,
  name        character varying NOT NULL,
  
  UNIQUE(name)
);

CREATE TABLE people
(
  id integer PRIMARY KEY,
  first_name  character varying NOT NULL,
  last_name   character varying NOT NULL,
  email character varying,
  phone integer,
  UNIQUE(first_name,last_name)
);

-- Relations between the above tables
CREATE TABLE ownership
(
  id          integer PRIMARY KEY,
  id_book     integer NOT NULL,
  id_people   integer NOT NULL,
  
  FOREIGN KEY(id_book)     REFERENCES book(id) ON DELETE CASCADE,
  FOREIGN KEY(id_people)   REFERENCES people(id) ON DELETE CASCADE
);

CREATE TABLE borrowings
(
  id          integer PRIMARY KEY,
  id_book     integer NOT NULL,
  id_people   integer NOT NULL,
  start_date  character varying DEFAULT (date('now')), 
  end_date    character varying CHECK (end_date >= start_date),
  
  UNIQUE(id_book),
  FOREIGN KEY(id_book)     REFERENCES book(id) ON DELETE CASCADE,
  FOREIGN KEY(id_people)   REFERENCES people(id) ON DELETE CASCADE
);

CREATE TABLE book_R_author
(
  id          integer PRIMARY KEY,
  id_book     integer NOT NULL,
  id_author   integer NOT NULL,
  
  UNIQUE(id_book,id_author),
  FOREIGN KEY(id_book)     REFERENCES book(id) ON DELETE CASCADE,
  FOREIGN KEY(id_author)   REFERENCES author(id) ON DELETE CASCADE
);

CREATE TABLE book_R_tag
(
  id          integer PRIMARY KEY,
  id_book     integer NOT NULL,
  id_tag      integer NOT NULL,
  
  UNIQUE(id_book,id_tag),
  FOREIGN KEY(id_book)  REFERENCES book(id) ON DELETE CASCADE,
  FOREIGN KEY(id_tag)   REFERENCES tag(id) ON DELETE CASCADE
);

-- POPULATING DATABASE WITH DEFAULT DATA
-- ORDER OF POPULATING
-- people 
-- author         
-- book           
-- book_R_author  
-- book_R_people  


INSERT INTO "people" VALUES
(1,'Daniel','Pęcak','daniel.pecak@gmail.com',693307789),
(2,'Karolina','Pęcak','karolina.suszynska@gmail.com',694292347),
(3,'Ada','Borowa','ada.borowa@gmail.com','');

INSERT INTO "tag"(name) VALUES
('nauka'),('fizyka'),('matematyka'),
('encyklopedia'),('podręcznik'),('popularne'),
('dzieci'),('poradnik'),('podróże');




COMMIT;

PRAGMA FOREIGN_KEYS=ON;