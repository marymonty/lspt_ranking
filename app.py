"""Starting falcon and adding our endpoint to the path.

We call our startup function to start the server, set our api application,
and add our endpoint route that is able to be called by other teams.
"""
import falcon

from .src.calling import Query
from .src.startup import startup

startup()

api = application = falcon.API()

application.req_options.auto_parse_form_urlencoded=True

ranking = Query()
api.add_route('/search', ranking)
