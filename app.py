import falcon

from .src.calling import Query
from .src.startup import startup

startup()

api = application = falcon.API()

application.req_options.auto_parse_form_urlencoded=True

ranking = Query()
api.add_route('/search', ranking)