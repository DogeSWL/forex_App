from flask import Flask, redirect, render_template
from app import app, db
from models import Users, FxSymbols
from utilFuncs import forex_forge, randFuncs
from views import quota

import time, datetime

@app.route('/converter')
def converterPage():
    return render_template('converter.html')

@app.route('/index')
def home():
    fxSymb = FxSymbols.query.all()
    a = ""

    # check to see if table is empty
    # empty sequences are false
    if not fxSymb:
        a = "list is empty"
        add_FxSymb = randFuncs.listToLongString(forex_forge.getSymbols())
        add_utcStamp = datetime.datetime.now(datetime.timezone.utc)

        fs = FxSymbols(symbFx=add_FxSymb, lastUpdated=add_utcStamp)
        db.session.add(fs)
        db.session.commit()
    else:
        a = fxSymb

    # getting coordinated universal time(UTC)
    utcTime = datetime.datetime.now(datetime.timezone.utc)
    return render_template('index.html', utcTime=utcTime, fxSymb=a)

@app.route('/')
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
