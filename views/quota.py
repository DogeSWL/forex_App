from flask import render_template
from app import app
from utilFuncs import forex_forge

@app.route('/quota')
def quotaPage():
    quota = forex_forge.getForgeQuota()
    return render_template('quota.html',quota=quota)
