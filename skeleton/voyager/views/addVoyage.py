
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape
from flask import redirect

from voyager.db import get_db, execute

def views(bp):
    def addvoyagefunc(conn, s_id, b_id, date):
        return execute(conn, f"insert into Voyages (sid, bid, date_of_voyage) values ('{s_id}', '{b_id}', '{date}')")

    @bp.route("/addVoyage", methods=['GET','POST'])
    def addvoyagepage():
        if request.method == 'GET':
            return render_template("addvoyage.html")
        if request.method == 'POST':
            with get_db() as conn:
                s_id = request.form['s_id']
                b_id = request.form['b_id']
                date = request.form['date']
                addvoyagefunc(conn, s_id, b_id, date)
        return redirect('/voyages')

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



    
