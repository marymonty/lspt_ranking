import falcon

from .src.calling import Resource
from .src.startup import startup

startup()

api = application = falcon.API()

ranking = Resource()
api.add_route('/ranking', ranking)