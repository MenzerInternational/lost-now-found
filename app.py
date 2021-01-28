from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def ufo(error):
    return render_template('base.html', ufo=error), 404
