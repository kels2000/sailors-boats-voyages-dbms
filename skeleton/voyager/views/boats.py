
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def boats(conn):
    return execute(conn, "SELECT b.bid, b.name, b.color FROM Boats AS b")

def boatsSailedBy(conn, s_name):
    return execute(conn, f"select distinct Boats.name as 'Boat Name' from Boats inner join Voyages on Boats.bid = Voyages.bid inner join Sailors on \
        Sailors.sid = Voyages.sid where Sailors.name = '{s_name}'")

def boatPopularity(conn):
    return execute(conn, "select Boats.name, count(*) as '# of reservations' from Boats inner join Voyages on Boats.bid = Voyages.bid group by Boats.name order by count(*) desc")

def views(bp):
    @bp.route("/boats")
    def _boats():
        with get_db() as conn:
            rows = boats(conn)
        return render_template("table.html", name="boats", rows=rows)

    @bp.route("/boats/sailed-by", methods=["GET", "POST"])
    def sailedByPage():
        if request.method == 'POST':
            with get_db() as conn:
                s_name = request.form["sailor-name"]
                rows = boatsSailedBy(conn, s_name)
            return render_template("table.html", name=s_name + ' sailed:', rows=rows)

    @bp.route("/boats/by-popularity")
    def boatPopularityPage():
        with get_db() as conn:
            rows = boatPopularity(conn)
        return render_template("table.html", name="Boats Ranked by Popularity", rows=rows)
