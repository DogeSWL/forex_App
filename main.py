from flask import redirect, render_template
from app import app, db
from utilFuncs import randFuncs, forex_forge
from models import FxSymbols, MarketStatus
from views import quota, symRate

import datetime

@app.route('/index')
def home():
    check_mktStatus = MarketStatus.query.all()
    fxSymb = FxSymbols.query.all()

    if not check_mktStatus:
        add_mktStatus = forex_forge.marketStatus()
        add_utcStamp = datetime.datetime.now(datetime.timezone.utc)

        c_ms = MarketStatus(mktStatus=add_mktStatus, lastUpdated=add_utcStamp)
        db.session.add(c_ms)
        db.session.commit()

    # check to see if table is empty (empty sequences are false)
    # if table is empty, popluate table with current Forge FX list and UTC time
    if not fxSymb:

        # get symbols from Forge, sort it alphabetically and then turn list into a string
        add_FxSymb = randFuncs.listToLongString(sorted(forex_forge.getSymbols()))
        add_utcStamp = datetime.datetime.now(datetime.timezone.utc)

        fs = FxSymbols(symbFx=add_FxSymb, lastUpdated=add_utcStamp)
        db.session.add(fs)
        db.session.commit()
    # else:
    #     dbFxList = FxSymbols.query.first()
    #     rtnFxList = randFuncs.lngStringToList(dbFxList.symbFx)
    #
    #     #removeing empty item in row 0 of list
    #     rtnFxList.pop(0)

    return render_template('index.html')

@app.route('/')
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
