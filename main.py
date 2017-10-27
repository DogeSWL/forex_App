from flask import Flask, redirect, render_template

from app import app, db
from models import Users, FxSymbols

from views import quota

import time, datetime

@app.route('/converter')
def converterPage():
    return render_template('converter.html')

@app.route('/index')
def home():
    # getting coordinated universal time(UTC)
    utcTime = datetime.datetime.now(datetime.timezone.utc)
    return render_template('index.html', utcTime=utcTime)

@app.route('/')
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
