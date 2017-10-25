from flask import Flask, redirect, render_template
from utilFuncs import forex_forge

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/index')
def home():
    quota = forex_forge.getForgeQuota()
    return render_template('index.html', quota=quota)

@app.route('/')
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
