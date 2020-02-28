from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def sailors(conn):
    return execute(conn, "SELECT s.sid, s.name, s.age, s.experience FROM Sailors AS s")

def sailorsSailed(conn, b_name):
    return execute(conn, f"select distinct Sailors.name as 'Sailor Name' from Boats inner join Voyages on Boats.bid = Voyages.bid inner join Sailors on \
        Sailors.sid = Voyages.sid where Boats.name = '{b_name}'")

def sailorsSailedOnDate(conn, date):
    return execute(conn, f"select distinct Sailors.name as 'Sailor Name' from Boats inner join Voyages on Boats.bid = Voyages.bid inner join Sailors on \
        Sailors.sid = Voyages.sid where Voyages.date_of_voyage = '{date}'")

def sailorsSailedBoatColor(conn, b_color):
    return execute(conn, f"select distinct Sailors.name as 'Sailor Name' from Boats inner join Voyages on Boats.bid = Voyages.bid inner join Sailors on \
        Sailors.sid = Voyages.sid where Boats.color = '{b_color}'")

def views(bp):
    @bp.route("/sailors")
    def _get_all_sailors():
        with get_db() as conn:
            rows = sailors(conn)
        return render_template("table.html", name="sailors", rows=rows)

    @bp.route("/sailors/who-sailed", methods=["GET", "POST"])
    def sailorsSailedPage():
        if request.method == 'POST':
            with get_db() as conn:
                b_name = request.form["boat-name"]
                rows = sailorsSailed(conn, b_name)
            return render_template("table.html", name=b_name + ' reserved by:', rows=rows)

    @bp.route("/sailors/who-sailed-on-date", methods=["GET", "POST"])
    def sailorsSailedOnDatePage():
        if request.method == 'POST':
            with get_db() as conn:
                date = request.form["date"]
                rows = sailorsSailedOnDate(conn, date)
            return render_template("table.html", name= 'Reserved on: ' + date, rows=rows)
  
    @bp.route("/sailors/who-sailed-on-boat-of-color", methods=["GET", "POST"])
    def sailorsSailedBoatColorPage():
        if request.method == 'POST':
            with get_db() as conn:
                b_color = request.form["boat-color"]
                rows = sailorsSailedBoatColor(conn, b_color)
            return render_template("table.html", name= 'Boat Color: ' + b_color, rows=rows)