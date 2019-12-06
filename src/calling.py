import json

import falcon
from .controller import GET

from .errors import EndpointException, ServerErrorCode

CORRECT_REQUEST = "ERROR: Query paramater must be a string of length greater than 0\n"


class Query(object):

    def on_post(self, req, resp):
        # Extract the query and fields from the request.
        bad_req = False
        try:
            to_rank = req.get_param('query', required=True)
            n_results = req.get_param('results', required=False)
            if n_results == None:
                n_results = 50
        except ValueError:
            bad_req = True

        # Check that the query is well-formed.
        if bad_req or to_rank == '' or \
            not isinstance(to_rank, str):
            resp.body = CORRECT_REQUEST
            resp.status = falcon.HTTP_400
        else:
            try:
                results = GET(to_rank, n_results)
            except EndpointException as e:
                resp.status = falcon.HTTP_503
                resp.body = "ERROR: Could not connect to endpoint %s\n" % e.endpoint
                return
            except ServerErrorCode as e:
                resp.status = falcon.HTTP_503
                resp.body = "ERROR: Connect to endpoint %s returned a non-200 code\n" % e.endpoint
                return

            # Create a JSON representation of the resource.
            resp.body = json.dumps(results, ensure_ascii=False)

            resp.status = falcon.HTTP_200
