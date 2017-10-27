from flask import Flask, redirect, render_template
from utilFuncs import forex_forge

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/quota')
def quotaPage():
    quota = forex_forge.getForgeQuota()
    return render_template('quota.html',quota=quota)

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/')
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
