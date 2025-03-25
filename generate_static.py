#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import flask
from gui import book


@renderAndsave
def bookbook(bookID):
    return book(bookID)

bookbook('1')
