
from flask import Blueprint

from voyager.views import index
from voyager.views import sailors
from voyager.views import boats
from voyager.views import voyages
from voyager.views import addBoat
from voyager.views import addSailor
from voyager.views import addVoyage

blueprint = Blueprint('views', __name__)
index.views(blueprint)
sailors.views(blueprint)
boats.views(blueprint)
voyages.views(blueprint)
addBoat.views(blueprint)
addSailor.views(blueprint)
addVoyage.views(blueprint)

def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')

