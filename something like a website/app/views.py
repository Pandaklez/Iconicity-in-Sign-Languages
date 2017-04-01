from flask import render_template, redirect, url_for, request, flash
from app import app, db, models
from .models import *

import json
import os.path
import re

@app.route('/')
def home():
    x = url_for('map')
    tabl = url_for('table')
    return render_template('base.html',
                           table=tabl,
                           mapp=x)

@app.route('/table')
def table():
    tabl = url_for('table')
    x = url_for('map')
    
    first_table = models.Base.query.all()
    second_table = models.Languages.query.all()

#    mapp = models.Base.query.filter_by(word='bicycle').first().template
#    x = url_for('map')
    return render_template('table.html',
                           title='Table',
                           base=first_table,
                           lang=second_table,
                           table=tabl)
@app.route('/map')
def map():
    tabl = url_for('table')
    x = url_for('map')
    
    mapp = models.Base.query.filter_by(word='bicycle').first().template
    #'\'' + mapp + '\''
    return render_template('bicycle.html',
                           title='Map',
                           mapp=x,
                           table=tabl)
