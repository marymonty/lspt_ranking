import falcon

from .src.calling import Resource
from .src.startup import startup

startup()

api = application = falcon.API()

application.req_options.auto_parse_form_urlencoded=True

ranking = Resource()
api.add_route('/search', ranking)