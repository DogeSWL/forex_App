from flask import render_template
from app import app, db
from models import FxSymbols
from utilFuncs import randFuncs, forex_forge

import datetime

@app.route('/fxRate', methods=['GET'])
def ratePage():

    return render_template('fxRate.html')
