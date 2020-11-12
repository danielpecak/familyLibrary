#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Functions for creating a LOG file
from datetime import datetime

LOG_FILENAME = 'library.log'
DEBUG_LEVEL  = 4 # 0:silent mode, 
                 # 1: errors
                 # 2: errors and warnings
                 # 3: says what it does
PRINTOUT_LEVEL = 3 # 0:silent mode, 
                 # 1: errors
                 # 2: errors and warnings
                 # 3: says what it does

def create():
    add("The logfile has been created.",3)
    
    
def add(message,level):
    """Desc """
    if level not in (1,2,3,4):
        add("argument LEVEL in add() function out of range: it should have value 1,2,3 and has %d."%(level,),1)
        return
    # message=message.decode('asci')
    keyword=('','ERROR:','WARNING:','INFO:','DEBUG:')
    if level <= DEBUG_LEVEL:
        now   = datetime.now()
        stamp = now.strftime('%Y-%m-%d, %H:%M:%S')
        f = open(LOG_FILENAME, "ab+")
        f.write(("# [%s] %s %s\n"%(stamp,keyword[level],message)).encode('utf-8'))
        f.close()
    if level <= PRINTOUT_LEVEL: print("# %s %s"%(keyword[level], message))
        


# add("The database has been created.",3)
# add("Warning",2)
# add("Error",1)
# add("Error",0)
# add("Error",4)

    