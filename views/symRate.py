from flask import render_template
from app import app
from models import FxSymbols
from utilFuncs import randFuncs

import datetime

@app.route('/symRate', methods=['GET'])
def symbPage():
    dbFxList = FxSymbols.query.first()
    rtnFxList = randFuncs.lngStringToList(dbFxList.symbFx)

    #removeing empty item in row 0 of list
    rtnFxList.pop(0)

    # current coordinated universal time(UTC)
    utcTime = datetime.datetime.now(datetime.timezone.utc)

    return render_template('symRate.html', utcTime=utcTime, dbFxList=dbFxList, fxList=rtnFxList)
