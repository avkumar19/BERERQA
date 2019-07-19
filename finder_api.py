#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:26:39 2019

@author: avinash
"""

from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)
import finder_core_v1 as fp
sol = fp.finder("Interface design")
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/corporates')
def corporates():
    return render_template('corporates.html')

@app.route('/startups')
def startups():
    return render_template('startups.html',startups = sol)

@app.route('/startup/<string:name>/')
def startup(name):
    start_up_data = fp.finder(name)
    return jsonify({'data':start_up_data})
    

if __name__ == '__main__':
    app.run(debug=True)