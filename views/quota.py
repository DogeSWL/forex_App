from flask import render_template, redirect
from app import app, db
from utilFuncs import forex_forge
from models import MarketStatus

import datetime

@app.route('/quota')
def quotaPage():
    # query MarketStatus table and grab data in the first row
    mktStatus = MarketStatus.query.first()

    # if table is empty, grab current market status and current utc timezone
    # add and commit them into MarketStatus table
    # redirect back to "/quota" route
    if not mktStatus:
        add_mktStatus = forex_forge.marketStatus()
        add_utcStamp = datetime.datetime.now(datetime.timezone.utc)

        c_ms = MarketStatus(mktStatus=add_mktStatus, lastUpdated=add_utcStamp)
        db.session.add(c_ms)
        db.session.commit()
        return redirect('/quota')

    mktStatus_OC = "Closed"
    quota = forex_forge.getForgeQuota()

    # if mktStatus in MarketStatus is 1 (open), set mktStatus_OC to "open"
    if mktStatus.mktStatus == 1:
        mktStatus_OC = "Open"

    return render_template('quota.html',quota=quota, mktStatus_lastUpdated=mktStatus.lastUpdated, mktStatus_OC=mktStatus_OC)
