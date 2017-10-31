from flask import redirect, render_template
from app import app
from views import quota, fxSymb

@app.route('/converter')
def converterPage():
    return render_template('converter.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/')
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
