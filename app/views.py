from flask import render_template, redirect, flash
from app import app
from app.models import Options
from flask import request
from formulas import *
import json

@app.route('/')
def index():
    form = Options(request.form)
    return render_template("index.html",
        title = 'Home',
        form = form,
        L = [0,0,0,0,0,0,0])

@app.route('/results', methods=['POST'])
def results():
    form = Options(request.form)
    if form.validate():
    
        w = form.weight.data
        r = form.reps.data
        w, r = float(w), float(r)
        L = [epley(w,r),brzycki(w,r),lombardi(w,r), mayhew(w,r), lander(w,r), oconner(w,r), wathan(w,r)]
        return render_template("index.html",
            L = json.dumps(L),
            form = form,
            w = w,
            r = r)
    flash('For Weight enter a number between 20-100 lb and for Reps between 2-10')
    return redirect('/')