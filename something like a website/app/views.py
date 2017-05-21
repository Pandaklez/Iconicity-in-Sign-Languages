from flask import render_template, redirect, url_for, request, flash
from app import app, db

import json
import os.path
import re
import csv
import sqlite3

def get_wordcol():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute('SELECT word FROM t')
    result = cur.fetchall()
    return result

@app.route('/')
def home():
    tabl = url_for('table')
    stat = url_for('stat')
    home = url_for('home')

    return render_template('home.html',
                           table=tabl,
                           home=home,
                           stat=stat)

@app.route('/stat')
def stat():
    tabl = url_for('table')
    stat = url_for('stat')
    home = url_for('home')
    
    return render_template('stat.html',
                           home=home,
                           table=tabl,
                           stat=stat)

#def making_pages(html):
#    for el in html:
#        route = '/map/' + el
@app.route('/map/<word>')
def map():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute('SELECT word FROM t')
    words = cur.fetchall()
    for word in words:
        return render_template(word + '.html',
                               title='Map')

@app.route('/table')
def table():
    tabl = url_for('table')
    stat = url_for('stat')

    result = get_wordcol()
    arr = []
    for element in result:
        z = element[0]
        if z not in arr:
            arr.append(z)
    #global html
    html = []
    for e in arr:
        p = e + ".html"
        html.append(p)

    #making_pages(html)
        
    tb = []
    i = 0
    for n in html:
        k = url_for("map/<html[i]>")
        tb.append(k)
        i += 1
    
    return render_template('db_table.html',
                           title='Table',
                           tb=tb,
                           home=home,
                           table=tabl,
                           stat=stat,
                           words=arr)


