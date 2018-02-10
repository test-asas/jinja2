import os
import sqlite3
import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    con = sqlite3.connect('testdb')
    con.close()
    return render_template(index.html)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.methods == 'POST':
        date_time = datetime.datetime.today()
        msg = request.form['msg']
