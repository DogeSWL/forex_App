from flask import render_template, redirect, request
from app import app, db
from models import FxSymbols
from utilFuncs import randFuncs, forex_forge

import datetime

@app.route('/symRate', methods=['GET', 'POST'])
def symbPage():
    # query FxSymbols table and grab data in the first row
    dbFxList = FxSymbols.query.first()

    # if table is empty get symbols from Forge
    # sort list alphabetically and then turn into string
    # add and commit them into FxSymbols table
    # redirect back to "/symRate" route
    if not dbFxList:
        add_FxSymb = randFuncs.listToLongString(sorted(forex_forge.getSymbols()))
        add_utcStamp = datetime.datetime.now(datetime.timezone.utc)

        fs = FxSymbols(symbFx=add_FxSymb, lastUpdated=add_utcStamp)
        db.session.add(fs)
        db.session.commit()

        return redirect('/symRate')

    rtnFxList = randFuncs.lngStringToList(dbFxList.symbFx)

    #removeing empty item in row 0 of list
    rtnFxList.pop(0)

    # current coordinated universal time(UTC)
    utcTime = datetime.datetime.now(datetime.timezone.utc)

    if request.method == 'POST':
        searchItems = request.form['searchItems']
        new_searchItems = forex_forge.getFxPairs(searchItems)
    else:
        new_searchItems = ""

    return render_template('symRate.html', utcTime=utcTime, dbFxList=dbFxList,
                            fxList=rtnFxList, new_searchItems=new_searchItems)
