#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import os 
import sys
import db
import logger 

# TODO creata one INIT.py script
# TODO creata log file as well
# TODO ask if something is overwritten or deleted when new items are created

conn = db.connection()
cur  = conn.cursor() 
sql = open(db.INIT_SQL,'r').read()
cur.executescript(sql)

logger.add("Database has been created from SQL file %s"%(db.INIT_SQL),3)
# conn.commit()
conn.close()
logger.add("Database %s has been closed"%(db.DB_NAME),3)
