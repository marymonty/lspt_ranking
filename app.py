import falcon

from .calling import Resource

api = application = falcon.API()

ranking = Resource()
api.add_route('/ranking', ranking)