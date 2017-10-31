from app import db

class Users(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.CHAR(120), unique=True)
    pwd = db.Column(db.CHAR(120))
    forgeAPI_key = db.Column(db.CHAR(120))

    def __init__(self, username, pwd, forgeAPI_key):
        self.username = username
        self.pwd = pwd
        self.forgeAPI_key = forgeAPI_key

class FxSymbols(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    symbFx = db.Column(db.TEXT)
    lastUpdated = db.Column(db.TIMESTAMP)

    def __init__(self, symbFx, lastUpdated):
        self.symbFx = symbFx
        self.lastUpdated = lastUpdated
