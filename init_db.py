#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import os 
import sys
import db


conn = db.connection()
cur  = conn.cursor() 
sql = open(db.INIT_SQL,'r').read()
cur.executescript(sql)

print("# Database has been created from SQL file %s"%(db.INIT_SQL))
# conn.commit()
conn.close()
print("# Database %s has been closed"%(db.DB_NAME))
