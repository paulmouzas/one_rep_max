from flask import render_template
from app import app
from app.models import Options
from flask import request
from formulas import *
import json

options = Options()

@app.route('/')
def index():

    return render_template("index.html",
        title = 'Home',
        options = options,)

@app.route('/', methods=['POST'])
def results():
    w = request.form['weight']
    r = request.form['reps']
    w, r = float(w), float(r)
    
    L = [epley(w,r),brzycki(w,r),lombardi(w,r), mayhew(w,r), lander(w,r), oconner(w,r), wathan(w,r)]
    return render_template("index.html",
        L = json.dumps(L),
        options = options,
        w = w,
        r = r)