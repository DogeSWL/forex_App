from app import db

class Users(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.CHAR(120), unique=True)
    pwd = db.Column(db.CHAR(120))

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd

class FxSymbols(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    symbFx = db.Column(db.TEXT)
    lastUpdate = db.Column(db.TIMESTAMP)

    def __init__(self, symbFx, lastUpdate):
        self.symbFx = symbFx
        self.lastUpdate = lastUpdate