from flask import render_template
from app import app, db
from models import FxSymbols
from utilFuncs import randFuncs, forex_forge

import datetime

@app.route('/fxSymb', methods=['GET'])
def symbPage():
    fxSymb = FxSymbols.query.all()
    aMsg = ""

    # check to see if table is empty (empty sequences are false)
    # if table is empty, popluate table with current Forge FX list and UTC time
    if not fxSymb:
        aMsg = "list is empty"
        
        # get symbols from Forge, sort it alphabetically and then turn list into a string
        add_FxSymb = randFuncs.listToLongString(sorted(forex_forge.getSymbols()))
        add_utcStamp = datetime.datetime.now(datetime.timezone.utc)

        fs = FxSymbols(symbFx=add_FxSymb, lastUpdated=add_utcStamp)
        db.session.add(fs)
        db.session.commit()
    else:
        dbFxList = FxSymbols.query.first()
        rtnFxList = randFuncs.lngStringToList(dbFxList.symbFx)

        #removeing empty item in row 0 of list
        rtnFxList.pop(0)

    # current coordinated universal time(UTC)
    utcTime = datetime.datetime.now(datetime.timezone.utc)

    return render_template('fxSymb.html', utcTime=utcTime, dbFxList=dbFxList, fxList=rtnFxList)
