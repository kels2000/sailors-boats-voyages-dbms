
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape
from flask import redirect
from flask import flash
from flask import url_for

from voyager.db import get_db, execute

def views(bp):
    def addsailorfunc(conn, s_name, age, experience):
        return execute(conn, f"insert into Sailors (name, age, experience) values ('{s_name}', '{age}', '{experience}')")

    @bp.route("/addSailor", methods=['GET','POST'])
    def addsailorpage():
        if request.method == 'GET':
            return render_template("addsailor.html")
        if request.method == 'POST':
            with get_db() as conn:
                s_name = request.form['s_name']
                age = request.form['age']
                experience = request.form['experience'] 
                addsailorfunc(conn, s_name, age, experience)
        return redirect('/sailors')

    # def addboatfunc(conn, name, color):
    #     return execute(conn, f"insert into Boats (name, color) values ('{b_name}', '{b_color}')")
                 
    
    # def addboat():
    #     if request.method == 'POST':
    #         with get_db() as conn:
    #             b_name = request.form['b_name']
    #             b_color = request.form['b_color']
    #             addboatfunc(conn, b_name, b_color)
    #     print("Submitted")
    #     flash('New entry was successfully posted')
    #     return redirect('/boats')



    
